# Generated by Django 5.0.1 on 2024-02-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimeData",
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
                ("mal_id", models.IntegerField()),
                ("url", models.URLField()),
                ("images", models.CharField()),
                ("trailer", models.CharField()),
                ("titles", models.CharField()),
                ("typ", models.CharField()),
                ("source", models.CharField()),
                ("episodes", models.CharField()),
                ("status", models.CharField()),
                ("duration", models.CharField()),
                ("aired", models.CharField()),
                ("rating", models.CharField()),
                ("genre", models.CharField()),
                ("synopsis", models.CharField()),
                ("rank", models.CharField()),
                ("popularity", models.CharField()),
            ],
            options={
                "db_table": "Anime_daatabase",
            },
        ),
    ]
