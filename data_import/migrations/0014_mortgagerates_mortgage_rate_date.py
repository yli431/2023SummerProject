# Generated by Django 5.0 on 2024-02-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0013_remove_meanhousevaluesuburbschch_primary_key_of_suburbs_chch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mortgagerates',
            name='mortgage_rate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
