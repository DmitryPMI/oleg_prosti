# Generated by Django 2.1.2 on 2018-10-19 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181019_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularevents',
            name='slug',
        ),
    ]