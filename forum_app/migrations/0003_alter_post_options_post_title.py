# Generated by Django 4.2.2 on 2023-06-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0002_remove_post_message_post_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
