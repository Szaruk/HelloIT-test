# Generated by Django 3.1.14 on 2022-04-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0061_auto_20220401_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
