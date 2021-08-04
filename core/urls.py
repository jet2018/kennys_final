# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),          # Django admin route
    path("", include("authentication.urls")),  # Auth routes - login
    path("", include("app.urls")),             # UI Kits Html files
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path("iprestrict/", include('iprestrict.urls', namespace='iprestrict')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
