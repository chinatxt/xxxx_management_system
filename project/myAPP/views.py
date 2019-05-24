# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

import time
import datetime
from .models import *

def index(request):
    return render_to_response('index.html')

def rooms(request):
    roomList=Room.objects.all()
    return render_to_response('rooms.html',{'roomList':roomList})
