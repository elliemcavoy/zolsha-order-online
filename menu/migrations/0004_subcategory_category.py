# Generated by Django 3.2 on 2022-01-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20220109_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category'),
        ),
    ]
