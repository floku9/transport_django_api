# Generated by Django 4.2.6 on 2023-10-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transport_api", "0003_alter_company_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="trucks",
            field=models.ManyToManyField(blank=True, to="transport_api.truck"),
        ),
    ]