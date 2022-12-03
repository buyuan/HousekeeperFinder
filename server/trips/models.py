import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from datetime import datetime

class User(AbstractUser):
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None

# add for service category
class serviceDetail(models.Model):
    name =models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trip(models.Model):
    REQUESTED = 'REQUESTED'
    STARTED = 'STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (STARTED, STARTED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pick_up_address = models.CharField(max_length=255,verbose_name = 'housekeeper_address',default= "fake")
    drop_off_address = models.CharField(max_length=255,verbose_name = 'customer_addreee')
    status = models.CharField(max_length=20, choices=STATUSES, default=REQUESTED)
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_driver',
        verbose_name = 'housekeeper'
    )
    rider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_rider',
        verbose_name = 'customer'
    )
    #job_time = models.DateTimeField(default ="Dec. 1, 2022, 7:51 a.m." )
    #add service content and price, 
    servicePrice = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default =100)
    #tempararily donot use it
    serviceCategory = models.ForeignKey('serviceDetail', on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name = 'Category')
    
    RoomClearing = 'RoomClearing'
    WalkingDog = 'WalkingDog'
    GardenClearing = 'GardenClearing'
    CarWash = 'CarWash'
    
    RequestCategory = (
        (RoomClearing,RoomClearing ),
        (WalkingDog, WalkingDog),
        (GardenClearing, GardenClearing),
        (CarWash, CarWash),
    )
    serviceCategory_new = models.CharField(max_length=40, choices=RequestCategory, default=RoomClearing, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('trip:trip_detail', kwargs={'trip_id': self.id})
