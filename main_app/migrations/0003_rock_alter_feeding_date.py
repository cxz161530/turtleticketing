from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_feeding"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="feeding",
            name="date",
            field=models.DateField(verbose_name="feeding date"),
        ),
    ]