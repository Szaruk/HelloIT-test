# Generated by Django 3.1.6 on 2021-05-26 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0036_auto_20210526_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Osoba', 'verbose_name_plural': 'Osoby'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posty'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projekt', 'verbose_name_plural': 'Projekty'},
        ),
        migrations.AlterModelOptions(
            name='projectdata',
            options={'verbose_name': 'Podpunkt Projektu', 'verbose_name_plural': 'Podpunkty Projektów'},
        ),
    ]
