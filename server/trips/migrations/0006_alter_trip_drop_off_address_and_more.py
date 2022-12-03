# Generated by Django 4.1.3 on 2022-11-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_servicedetail_trip_serviceprice_trip_servicecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='drop_off_address',
            field=models.CharField(max_length=255, verbose_name='customer_addreee'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pick_up_address',
            field=models.CharField(max_length=255, verbose_name='housekeeper_address'),
        ),
    ]