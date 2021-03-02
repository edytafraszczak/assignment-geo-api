from django.db import models


# Create your models here.
class GeoLocation(models.Model):
    ip_or_url = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    continent_code = models.CharField(max_length=255)
    continent_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.JSONField(null=True)
    time_zone = models.JSONField(null=True)
    currency = models.JSONField(null=True)
    connection = models.JSONField(null=True)
