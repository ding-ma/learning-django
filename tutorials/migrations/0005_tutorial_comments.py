# Generated by Django 3.0.7 on 2020-06-26 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200626_1556'),
        ('tutorials', '0004_auto_20200626_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorial_comments', to='comment.Comment'),
        ),
    ]
