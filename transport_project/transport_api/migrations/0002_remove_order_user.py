# Generated by Django 4.2.6 on 2023-10-21 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
