# Generated by Django 3.1.6 on 2021-06-11 11:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0039_auto_20210611_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug_field',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique_with=('create_date',)),
        ),
    ]
