# Generated by Django 3.2.25 on 2024-06-29 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0009_app_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_image',
            name='app_img',
        ),
    ]
