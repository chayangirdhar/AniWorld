# Generated by Django 5.0.1 on 2024-02-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0003_animedaatabase_delete_animedata"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnimeDatabase",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("mal_id", models.BigIntegerField(blank=True)),
                ("title", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
                ("images", models.TextField(blank=True, null=True)),
                ("trailer", models.TextField(blank=True, null=True)),
                ("titles", models.TextField(blank=True, null=True)),
                ("type", models.TextField(blank=True, null=True)),
                ("episodes", models.BigIntegerField(blank=True, null=True)),
                ("aired", models.TextField(blank=True, null=True)),
                ("source", models.TextField(blank=True, null=True)),
                ("status", models.TextField(blank=True, null=True)),
                ("duration", models.TextField(blank=True, null=True)),
                ("rating", models.TextField(blank=True, null=True)),
                ("synopsis", models.TextField(blank=True, null=True)),
                ("rank", models.BigIntegerField(blank=True, null=True)),
                ("popularity", models.BigIntegerField(blank=True, null=True)),
                ("genre", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "Anime_database",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="AnimeDaatabase",
        ),
    ]