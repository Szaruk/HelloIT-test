# Generated by Django 3.1.6 on 2021-04-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0027_auto_20210412_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]