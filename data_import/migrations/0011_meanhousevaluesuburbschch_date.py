# Generated by Django 5.0 on 2024-02-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0010_delete_averagehousevaluechch'),
    ]

    operations = [
        migrations.AddField(
            model_name='meanhousevaluesuburbschch',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
