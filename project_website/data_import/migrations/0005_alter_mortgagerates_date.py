# Generated by Django 5.0 on 2024-01-12 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0004_mortgagerates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mortgagerates',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
