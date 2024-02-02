# Generated by Django 2.2.24 on 2022-05-24 13:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0090_remove_duplicate_field_name_choices"),
    ]

    operations = [
        migrations.AddField(
            model_name="facilitylistitem",
            name="sector",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                help_text="The sector(s) for goods made at the facility",
                default=['Apparel'],
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="facilitylistitem",
            name="sector",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                help_text="The sector(s) for goods made at the facility",
                size=None,
            ),
        ),
    ]
