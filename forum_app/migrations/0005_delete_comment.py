# Generated by Django 4.2.2 on 2023-06-18 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
