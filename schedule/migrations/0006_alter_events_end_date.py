# Generated by Django 4.2.3 on 2023-07-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0005_alter_tournament_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]