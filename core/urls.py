# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),          # Django admin route
    path("", include("authentication.urls")),  # Auth routes - login
    path("", include("app.urls")),             # UI Kits Html files
]
