# Generated by Django 4.2.14 on 2024-08-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.CharField(max_length=100),
        ),
    ]
