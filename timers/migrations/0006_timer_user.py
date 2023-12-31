# Generated by Django 4.2.4 on 2023-08-24 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("timers", "0005_remove_timer_set_date_timer_set_datetime"),
    ]

    operations = [
        migrations.AddField(
            model_name="timer",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="timers",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
