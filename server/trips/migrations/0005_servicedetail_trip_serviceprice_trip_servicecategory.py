# Generated by Django 4.1.3 on 2022-11-29 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='servicePrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='serviceCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trips.servicedetail'),
        ),
    ]
