from employees.models import DailyPerfomance
from django.contrib import admin

# Register your models here.
admin.site.site_header = "TEAS ADMINISTRATOR"


class DailyPerformanceAdmin(admin.ModelAdmin):
    list_display = ['Employer',
                    'checked_in_at', 'checked_out_at', 'date', 'hours_worked', 'amount_earned']


admin.site.register(DailyPerfomance, DailyPerformanceAdmin)
