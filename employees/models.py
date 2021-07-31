from datetime import datetime, date
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from authentication.models import AddEmployer
from django.db import models
from django.db.models.base import Model
from djmoney.models.fields import MoneyField
from ckeditor.fields import RichTextField
from djmoney.models.managers import understands_money
# Create your models here.


class DailyPerfomance(models.Model):

    class Meta:
        verbose_name = "Daily perfomance"
        verbose_name_plural = "Daily perfomances"

    Employer = models.ForeignKey(AddEmployer, on_delete=models.CASCADE)
    checked_in_at = models.TimeField()
    checked_out_at = models.TimeField(null=True, blank=True)
    daily_coverage = RichTextField(
        null=True, help_text="What have you worked on today, please include -from -to times", blank=True)
    date = models.DateTimeField(auto_now=True)

    @property
    def hours_worked(self):
        hrs = 0
        if self.checked_out_at:
            c = datetime.combine(date.min, self.checked_out_at) - \
                datetime.combine(date.min, self.checked_in_at)
            secs = c.seconds
            hrs = int(secs/3600)
        return hrs

    @property
    def amount_earned(self):
        get_amount = AddEmployer.objects.get(pk=self.Employer.pk)
        # currency can be obtained with amount_currency
        amount = get_amount.hourly_charge.amount
        return 'UGX '+str(self.hours_worked * amount)

    def __str__(self):
        return self.Employer.user.username

    