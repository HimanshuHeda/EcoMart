# Generated by Django 4.2.6 on 2023-11-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_rename_status_order_delivery_order_placedorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(null=True, upload_to='order_images/'),
        ),
    ]
