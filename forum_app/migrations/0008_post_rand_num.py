# Generated by Django 4.2.2 on 2023-06-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0007_alter_comment_options_post_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rand_num',
            field=models.IntegerField(default=3, null=True),
        ),
    ]