# Generated by Django 4.2.4 on 2023-08-24 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("themes", "0002_theme_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="themes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]