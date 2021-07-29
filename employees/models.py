from authentication.models import AddEmployer
from django.db import models
from django.db.models.base import Model
from djmoney.models.fields import MoneyField


# Create your models here.


class DailyPerfomance(models.Model):

    class Meta:
        verbose_name = "Daily perfomance"
        verbose_name_plural = "Daily perfomances"

    Employer = models.ForeignKey(AddEmployer, on_delete=models.CASCADE)
    checked_in_at = models.TimeField()
    checked_out_at = models.TimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    @property
    def hours_worked(self):
        c = self.checked_out_at - self.checked_in_at
        secs = c.seconds
        hrs = int(secs / 3600)
        return hrs
    
    @property
    def amount_aerned(self):
        get_amount = AddEmployer.objects.get(pk = self.Employer.pk)
        
        self.hours_worked 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
