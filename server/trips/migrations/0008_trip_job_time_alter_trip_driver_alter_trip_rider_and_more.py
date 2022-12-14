# Generated by Django 4.1.3 on 2022-12-01 06:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_trip_servicecategory_new_alter_trip_serviceprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='job_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 6, 25, 3, 42448)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips_as_driver', to=settings.AUTH_USER_MODEL, verbose_name='housekeeper'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips_as_rider', to=settings.AUTH_USER_MODEL, verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='serviceCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trips.servicedetail', verbose_name='Category'),
        ),
    ]
