from employees.models import DailyPerfomance
from django.contrib import admin

# Register your models here.
admin.site.site_header = "TEAS ADMINISTRATOR"

class DailyPerfomanceAdmin(admin.ModelAdmin):
    list_display=['Employer', 'checked_in_at', 'checked_out_at', 'hours_worked', 'date']

admin.site.register(DailyPerfomance)