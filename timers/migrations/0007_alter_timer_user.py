# Generated by Django 4.2.4 on 2023-08-24 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("timers", "0006_timer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="timers",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]