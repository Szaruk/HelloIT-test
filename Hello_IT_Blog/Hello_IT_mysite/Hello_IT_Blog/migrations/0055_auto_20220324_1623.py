# Generated by Django 3.1.14 on 2022-03-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0054_auto_20220324_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherproject',
            name='full_info',
            field=models.TextField(default='', help_text='Pełna informacja o projekcie', verbose_name='Pełna informacja'),
        ),
        migrations.AddField(
            model_name='project',
            name='full_info',
            field=models.TextField(default='', help_text='Pełna informacja o projekcie', verbose_name='Pełna informacja'),
        ),
    ]
