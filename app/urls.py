# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

app_name= 'app_view'
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('daily_coverage', views.UpdateAddDailyCoverage, name="daily_coverage"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
