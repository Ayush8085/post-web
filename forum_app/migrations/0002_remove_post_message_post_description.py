# Generated by Django 4.2.2 on 2023-06-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
