# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from authentication.models import AddEmployer
from django.contrib import admin


class AddEmployerAdmin(admin.ModelAdmin):
    fields = ['user', 'check_in_time',
              'check_out_time', 'hourly_charge']
    list_display = ['user', 'check_in_time',
                    'check_out_time', 'date', 'hourly_charge']
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name', 'hourly_charge']
    list_filter = ['date', 'user__username']


admin.site.register(AddEmployer, AddEmployerAdmin)
