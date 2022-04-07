# Generated by Django 3.1.6 on 2021-04-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0029_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='people_tag',
            field=models.CharField(choices=[('rppg', 'Team RPPG'), ('racing', 'Team Racing'), ('brawl', 'Team Brawl'), ('django', 'Team Django'), ('java1', 'Team Java 1'), ('php1', 'Team PHP 1'), ('js1', 'Team JavaScript 1')], default='rppg', max_length=20),
        ),
    ]
