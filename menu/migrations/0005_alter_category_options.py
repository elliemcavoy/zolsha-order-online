# Generated by Django 3.2 on 2022-01-09 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_subcategory_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
