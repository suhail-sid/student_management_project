# Generated by Django 4.1.7 on 2023-07-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0003_staff_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff_notification",
            name="status",
            field=models.IntegerField(default=0, null=True),
        ),
    ]