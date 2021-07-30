
from authentication.models import AddEmployer
from django.contrib import admin


class AddEmployerAdmin(admin.ModelAdmin):
    fields = ['user', 'check_in_time',
              'check_out_time', 'job_title', 'hourly_charge', 'job_description']
    list_display = ['user', 'check_in_time',
                    'check_out_time', 'date', 'hourly_charge']
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name', 'hourly_charge']
    list_filter = ['date', 'user__username']


admin.site.register(AddEmployer, AddEmployerAdmin)
