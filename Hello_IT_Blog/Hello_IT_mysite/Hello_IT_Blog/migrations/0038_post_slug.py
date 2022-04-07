# Generated by Django 3.1.6 on 2021-06-11 11:19

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0037_auto_20210526_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from=models.CharField(max_length=255, verbose_name='Tytuł'), unique_with=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data utworzenia')),
        ),
    ]
