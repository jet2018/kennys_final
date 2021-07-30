from django.db.models import fields
from employees.models import DailyPerfomance
from django.forms import ModelForm


class MyCoverageForm(ModelForm):
    class Meta:
        model = DailyPerfomance
        fields = ['daily_coverage']
