import datetime

from django.views.generic.base import TemplateView
from django.shortcuts import render
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
    pass

def submit_tune(request):
    tune = Tune()
    tune.created_by = request.user
    tune.save()

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
