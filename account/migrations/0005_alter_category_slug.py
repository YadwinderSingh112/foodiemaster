# Generated by Django 4.1.1 on 2022-12-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_post_category_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=5, unique=True),
        ),
    ]
