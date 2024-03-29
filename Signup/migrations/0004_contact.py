# Generated by Django 4.2.3 on 2024-03-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Signup", "0003_usersignup_last_login_alter_usersignup_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
