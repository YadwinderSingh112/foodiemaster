# Generated by Django 4.1.3 on 2022-12-12 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_comment_email_post_likee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
