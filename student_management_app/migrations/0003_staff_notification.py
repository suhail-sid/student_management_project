# Generated by Django 4.1.7 on 2023-07-19 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0002_alter_customuser_user_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Staff_notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_management_app.staff",
                    ),
                ),
            ],
        ),
    ]