# Generated by Django 5.0 on 2024-02-07 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0019_rename_meanhousevaluesuburbschch_christchurchsuburbmeanhousevalue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChristchurchSuburbMeanHouseValue',
            new_name='ChristchurchSuburbMeanPropertyPrice',
        ),
    ]
