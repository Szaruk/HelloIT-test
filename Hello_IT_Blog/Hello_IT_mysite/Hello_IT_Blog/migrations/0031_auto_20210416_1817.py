# Generated by Django 3.1.6 on 2021-04-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0030_auto_20210414_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourproject',
            name='team_name',
            field=models.CharField(choices=[('rppg', 'Team RPPG'), ('racing', 'Team Racing'), ('brawl', 'Team Darkest Kombat'), ('django', 'Team Django')], default='rppg', help_text='Nazwa zespołu nie może przekraczać 30 znaków.', max_length=30),
        ),
        migrations.AlterField(
            model_name='people',
            name='people_tag',
            field=models.CharField(choices=[('rppg', 'Team RPPG'), ('racing', 'Team Racing'), ('brawl', 'Team Darkest Kombat'), ('django', 'Team Django')], default='rppg', max_length=20),
        ),
    ]
