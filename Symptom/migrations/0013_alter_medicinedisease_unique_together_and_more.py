# Generated by Django 4.2.3 on 2024-03-08 11:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Symptom", "0012_medicine_medicinedisease"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="medicinedisease",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="medicinedisease",
            name="disease",
        ),
        migrations.RemoveField(
            model_name="medicinedisease",
            name="medicine",
        ),
        migrations.DeleteModel(
            name="Medicine",
        ),
        migrations.DeleteModel(
            name="MedicineDisease",
        ),
    ]
