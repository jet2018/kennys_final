# Generated by Django 3.1.7 on 2021-07-30 10:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyperfomance',
            name='daily_coverage',
            field=ckeditor.fields.RichTextField(blank=True, help_text='What have you worked on today, please include -from -to times', null=True),
        ),
    ]
