# Generated by Django 2.1 on 2018-09-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishopapp', '0002_remove_item_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Status',
        ),
        migrations.AlterField(
            model_name='item',
            name='Description',
            field=models.TextField(max_length=10000),
        ),
    ]
