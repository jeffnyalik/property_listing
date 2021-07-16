from django.db import models
from datetime import datetime

class Realtors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Realtors'


    def __str__(self):
        return self.name