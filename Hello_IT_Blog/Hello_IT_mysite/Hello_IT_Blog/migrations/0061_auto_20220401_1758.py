# Generated by Django 3.1.14 on 2022-04-01 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0060_auto_20220401_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hello_IT_Blog.team', verbose_name='Nazwa drużyny'),
        ),
    ]
