from django.db import models
from realtors.models import Realtors
from django.utils.timezone import now

class Listings(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
        FOR_LEASE = 'For Lease'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        LAND = 'Land'
        TOWN_HOUSE = 'Town House'
        CONDO = 'Condo'
        PENT_HOUSE = 'Pent House'

    
    realtor = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    town = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sale_type = models.CharField(max_length=65, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=65, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField(default=0)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    list_date = models.DateTimeField(default=now, blank=True)
    is_published = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Listings'

    
    def __str__(self):
        return self.title

