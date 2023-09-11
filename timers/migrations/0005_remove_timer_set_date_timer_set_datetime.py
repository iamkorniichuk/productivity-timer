# Generated by Django 4.2.4 on 2023-08-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timers", "0004_alter_timer_task"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timer",
            name="set_date",
        ),
        migrations.AddField(
            model_name="timer",
            name="set_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="set datetime"
            ),
        ),
    ]