# Generated by Django 3.1.6 on 2021-03-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hello_IT_Blog', '0009_auto_20210225_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_div_id', models.CharField(max_length=20)),
                ('about_title', models.CharField(max_length=50)),
                ('about_content', models.TextField(default='')),
            ],
        ),
    ]