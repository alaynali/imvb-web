# Generated by Django 4.2.3 on 2023-07-18 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Announcments",
            new_name="Announcements",
        ),
    ]