# Generated by Django 3.1.6 on 2022-03-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0049_auto_20220209_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='people_tag',
            field=models.CharField(choices=[('rppg', 'Team RPPG'), ('python', 'Grupa Python'), ('flutter', 'Team Flutter'), ('unitya', 'Grupa Unity A'), ('unityb', 'Grupa Unity B'), ('overseer', 'Opiekun Koła'), ('unassigned', 'Nieprzypisany/na')], default='rppg', max_length=20, verbose_name='Drużyna'),
        ),
    ]