# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.forms import MyCoverageForm
import datetime
from employees.models import DailyPerfomance
from authentication.models import AddEmployer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
now = datetime.datetime.now()

today = now.date()
time = now.time()
year = now.year
month = now.month
day = now.day


@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'
    context['form'] = MyCoverageForm()
    context['emp'] = AddEmployer.objects.get(user=request.user)
    context['todays'] = DailyPerfomance.objects.get(
        Employer__user=request.user, date__day=day)
    try:
        context['yesto'] = DailyPerfomance.objects.get(
            Employer__user=request.user, date__day=day-1)
    except DailyPerfomance.DoesNotExist:
        context['yesto'] = None

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
