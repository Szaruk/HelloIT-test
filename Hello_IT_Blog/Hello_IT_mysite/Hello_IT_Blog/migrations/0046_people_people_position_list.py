# Generated by Django 3.1.6 on 2022-02-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0045_auto_20220203_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='people_position_list',
            field=models.CharField(choices=[('graphics_designer', 'Grafik'), ('programmer', 'Programista'), ('project_manager', 'Kierownik projektu'), ('sound_designer', 'Dźwękowiec'), ('writer', 'Scenarzysta'), ('public_relations', 'PR'), ('overseer', 'Opiekun Koła')], default='graphics_designer', max_length=25, verbose_name='Stanowisko'),
        ),
    ]
