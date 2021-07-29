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
    def amount_earned(self):

        return

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
