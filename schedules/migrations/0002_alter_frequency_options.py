# Generated by Django 4.2.4 on 2023-08-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="frequency",
            options={"verbose_name_plural": "frequencies"},
        ),
    ]
