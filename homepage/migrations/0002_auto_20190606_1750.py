# Generated by Django 2.2.1 on 2019-06-06 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ava',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ava',
        ),
    ]
