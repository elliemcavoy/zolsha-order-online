# Generated by Django 3.2 on 2022-01-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='res_number',
            field=models.CharField(default=0, editable=False, max_length=32),
        ),
    ]
