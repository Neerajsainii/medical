# Generated by Django 4.2.3 on 2024-03-08 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Symptom", "0011_diseasesymptom"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MedicineDisease",
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
                (
                    "disease",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Symptom.disease",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Symptom.medicine",
                    ),
                ),
            ],
            options={
                "unique_together": {("medicine", "disease")},
            },
        ),
    ]