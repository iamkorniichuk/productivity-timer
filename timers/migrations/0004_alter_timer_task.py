# Generated by Django 4.2.4 on 2023-08-06 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_task_theme"),
        ("timers", "0003_alter_timer_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timer",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="timers",
                to="tasks.task",
                verbose_name="task",
            ),
        ),
    ]
