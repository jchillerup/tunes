from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from .models import *

import datetime

def home(request):
    now = datetime.datetime.now()

    latest_tunes = Setting.objects.order_by('-id')[:10]
    
    context = {
        'timestamp': now,
        'latest_tunes': latest_tunes,
        }
    
    return render(request, 'index.html', context)

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

def tunes(request):
    context = {
        "tunes": Tune.objects.get()
        }
    
    return render(request, 'tunes.html', context)

def about(request):
    return render(request, 'about.html')

def add_tune(request):
    context = {"allowed_keys": SETTING_KEY_CHOICES}
    return render(request, 'add_tune.html', context)

def add_setting(request):
    pass


def fourohfour(request):
    return render(request, '404.html')
