# Generated by Django 4.2.3 on 2023-07-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0002_tournament_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
