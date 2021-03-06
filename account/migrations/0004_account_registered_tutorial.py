# Generated by Django 3.0.7 on 2020-06-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20200626_1648'),
        ('account', '0003_remove_account_registered_tutorials'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='registered_tutorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered_tutorial', to='tutorials.Tutorial'),
        ),
    ]
