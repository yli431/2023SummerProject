# Generated by Django 5.0 on 2024-02-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0012_remove_meanhousevaluesuburbschch_month_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='meanhousevaluesuburbschch',
            constraint=models.UniqueConstraint(fields=('suburb', 'date'), name='primary_key_of_suburbs_CHCH'),
        ),
    ]
