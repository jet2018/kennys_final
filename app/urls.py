# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

app_name = 'app_view'
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('payments', views.PaymentsListView, name="payments"),
    path('<str:username>/profile',
         views.ProfileView.as_view(), name="profile"),
    path('upload_image', views.UploadProfilePik,
         name="upload_image"),
    path('passwprd_reset', views.ResetPasword, name="passwprd_reset"),
    path('user_update', views.UserUpdate, name="user_update"),
    path('user_job_title', views.UserJobTitle, name="user_job_title"),
    path('user_phone', views.UserPhoneAndAddress, name="user_phone"),
    path('daily_coverage', views.UpdateAddDailyCoverage, name="daily_coverage"),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
