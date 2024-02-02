# Generated by Django 3.2.14 on 2022-07-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0095_auto_20220706_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedfield',
            name='value',
            field=models.JSONField(help_text='The value of the field. An  object with different structure for different fields.Numeric fields are stored as {"min": 1, "max": 2}.If there is a single numeric value, set both min and max to it.'),
        ),
        migrations.AlterField(
            model_name='facilitylistitem',
            name='processing_results',
            field=models.JSONField(default=list, help_text='Diagnostic details logged by background processing including details returned from the geocoder.'),
        ),
        migrations.AlterField(
            model_name='facilitymatch',
            name='results',
            field=models.JSONField(help_text='Diagnostic details from the matching process.'),
        ),
        migrations.AlterField(
            model_name='historicalextendedfield',
            name='value',
            field=models.JSONField(help_text='The value of the field. An  object with different structure for different fields.Numeric fields are stored as {"min": 1, "max": 2}.If there is a single numeric value, set both min and max to it.'),
        ),
        migrations.AlterField(
            model_name='historicalfacilitymatch',
            name='results',
            field=models.JSONField(help_text='Diagnostic details from the matching process.'),
        ),
    ]
