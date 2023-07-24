# Generated by Django 4.2.3 on 2023-07-24 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0006_alter_player_major"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="image",
            field=models.ImageField(default="profile_icon.png", upload_to="roster"),
        ),
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.CharField(
                choices=[
                    ("Illini 1s", "Illini 1s"),
                    ("Illini 2s", "Illini 2s"),
                    ("Illini 3s", "Illini 3s"),
                ],
                max_length=9,
            ),
        ),
    ]
