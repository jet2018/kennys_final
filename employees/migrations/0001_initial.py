# Generated by Django 3.1.7 on 2021-07-29 10:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_auto_20210729_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPerfomance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_in_at', models.TimeField()),
                ('checked_out_at', models.TimeField(blank=True, null=True)),
                ('daily_coverage', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.addemployer')),
            ],
            options={
                'verbose_name': 'Daily perfomance',
                'verbose_name_plural': 'Daily perfomances',
            },
        ),
    ]
