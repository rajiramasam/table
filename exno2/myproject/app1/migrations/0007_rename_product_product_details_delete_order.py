# Generated by Django 5.0.7 on 2024-08-03 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Product_Details',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
