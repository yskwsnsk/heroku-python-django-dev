# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(req):
##    return HttpResponse('INDEX')
    return render(req, 'index.html')
