# Generated by Django 4.2.4 on 2023-09-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_task_previous_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(
                blank=True, default="", max_length=64, verbose_name="name"
            ),
        ),
    ]
