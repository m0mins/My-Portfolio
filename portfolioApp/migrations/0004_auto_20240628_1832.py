# Generated by Django 3.2.25 on 2024-06-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0003_professionalexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalexperience',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]
