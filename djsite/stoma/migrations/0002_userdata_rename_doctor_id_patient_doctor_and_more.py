# Generated by Django 4.2.16 on 2024-10-26 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("stoma", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserData",
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
                ("phone", models.CharField(max_length=255)),
                ("personal_account", models.IntegerField()),
                ("family_account", models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name="patient",
            old_name="doctor_id",
            new_name="doctor",
        ),
        migrations.AddField(
            model_name="patient",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stoma.userdata",
            ),
        ),
    ]
