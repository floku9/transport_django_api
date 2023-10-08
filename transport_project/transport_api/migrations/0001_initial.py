# Generated by Django 4.2.6 on 2023-10-07 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("contact_number", models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name="Truck",
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
                ("model", models.CharField(max_length=255)),
                (
                    "lifting_capacity",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Warehouse",
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
                ("address", models.CharField(max_length=255)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transport_api.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("goods", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "destination_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination_warehouse",
                        to="transport_api.warehouse",
                    ),
                ),
                (
                    "performer_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transport_api.company",
                    ),
                ),
                (
                    "starting_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="starting_warehouse",
                        to="transport_api.warehouse",
                    ),
                ),
                (
                    "truck",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transport_api.truck",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="trucks",
            field=models.ManyToManyField(to="transport_api.truck"),
        ),
    ]
