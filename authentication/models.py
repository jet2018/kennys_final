

from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from django.conf import settings
from django.db import models

# Create your models here.


class AddEmployer(models.Model):

    user = models.OneToOneField(User,  verbose_name="Employer",
                                on_delete=models.CASCADE)
    check_in_time = models.TimeField(null=True, blank=True)
    job_title = models.CharField(max_length=250, blank=True)
    user_image = models.ImageField('users', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    check_out_time = models.TimeField(
        null=True, help_text="Time should be expressed in 24 hours eg 17:00:00 if you want to achieve pm, default is am", blank=True)
    date = models.DateField(auto_now_add=True)
    is_online = models.BooleanField(default=False)
    hourly_charge = MoneyField(
        max_digits=10, decimal_places=3, blank=True, null=True, default_currency=None)
    job_description = RichTextField(
        null=True, help_text="What is this worker supposed to do in a day", blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

# signal for auto creating profile instance after creating a new user


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        AddEmployer.objects.create(user=kwargs['instance'])
