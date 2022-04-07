# Generated by Django 3.1.6 on 2022-02-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0048_auto_20220209_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='people_hobby',
        ),
        migrations.RemoveField(
            model_name='people',
            name='people_info',
        ),
        migrations.RemoveField(
            model_name='people',
            name='people_position',
        ),
        migrations.AddField(
            model_name='people',
            name='people_portfolio',
            field=models.TextField(blank=True, default='', help_text='Po kliknięciu w kafelek osoby, nastąpi przekierowanie na podany link', verbose_name='Link do portfolio'),
        ),
    ]