# Generated by Django 3.0.7 on 2020-06-26 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='registered_users',
        ),
    ]
