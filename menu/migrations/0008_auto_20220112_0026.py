# Generated by Django 3.2 on 2022-01-12 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
