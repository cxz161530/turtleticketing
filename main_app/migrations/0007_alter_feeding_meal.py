# Generated by Django 4.2.14 on 2024-08-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_feeding_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.TextField(),
        ),
    ]