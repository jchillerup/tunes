import datetime

from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
    now = datetime.datetime.now()

    latest_tunes = Setting.objects.order_by('-id')[:10]
    
    context = {
        'user': request.user,
        'timestamp': now,
        'latest_tunes': latest_tunes,
        }
    
    return render(request, 'index.html', context)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
        else:
            # deal with inactive users
            pass

    else:
        # invalid login
        pass
    
    return home(request)

def logout(request):
    auth_logout(request)
    return home(request)

def tune(request, tune_id):
    tune_id = int(tune_id)

    tune = Tune.objects.get(id=tune_id)
    settings = Setting.objects.filter(tune__id=tune_id)

    context = {
        'tune': tune,
        'settings': settings,
        }
    
    return render(request, 'view_tune.html', context)

# Return the tune as an ABC file
def tune_abc(request, tune_id):
    # Return alll settings
    tune = Tune.objects.get(id=tune_id)
    return HttpResponse(tune.__str__())

def submit_tune(request):
    tunes_user, existed_user = TunesUser.objects.get_or_create(user = request.user)
    tune_type, existed_type = TuneType.objects.get_or_create(name = request.POST.get('type'))

    if not existed_type:
        tune_type.standard_unit_note = request.POST.get('unit_note')
        # tune_type.standard_tempo = request.POST.get('tempo')
    
    tune = Tune()
    tune.title = request.POST.get('title')
    tune.composer = request.POST.get('composer')
    tune.origin = request.POST.get('origin')
    tune.created_by = tunes_user
    tune.type = tune_type
    tune.save()

    setting = Setting()
    setting.tune = tune
    setting.meter = request.POST.get('meter')
    setting.unit_note = request.POST.get('unit_note')
    setting.key = request.POST.get('key')
    setting.staves = request.POST.get('staves')
    setting.created_at = datetime.datetime.now()
    setting.last_modified = datetime.datetime.now()
    setting.created_by = tunes_user
    setting.save()

    return redirect(tune)

def tunes(request):
    try:
        context = {
            "tunes": Tune.objects.get()
            }
    except ObjectDoesNotExist:
        context  = {
            "tunes": []
            }
    
    return render(request, 'tunes.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def add_tune(request):
    context = {"allowed_keys": SETTING_KEY_CHOICES}
    return render(request, 'add_tune.html', context)

def add_setting(request):
    pass


def fourohfour(request):
    return render(request, '404.html')
