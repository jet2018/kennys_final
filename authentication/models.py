

from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.


class AddEmployer(models.Model):

    user = models.ForeignKey(User, verbose_name="Employer",
                             on_delete=models.CASCADE)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    hourly_charge = MoneyField(
        max_digits=10, decimal_places=3, null=True, default_currency=None)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Add employer'
        verbose_name_plural = 'Add employers'
