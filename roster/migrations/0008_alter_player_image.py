# Generated by Django 4.2.3 on 2023-07-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0007_alter_player_image_alter_player_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="image",
            field=models.ImageField(
                blank=True, default="profile_icon.png", upload_to="roster"
            ),
        ),
    ]