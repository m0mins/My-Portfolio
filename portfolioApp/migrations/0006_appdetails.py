# Generated by Django 3.2.25 on 2024-06-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0005_profile_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('clinet', models.CharField(blank=True, max_length=100, null=True)),
                ('project_date', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
