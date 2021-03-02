from django.contrib import admin

# Register your models here.
from api.models import GeoLocation


@admin.register(GeoLocation)
class GeoLocationAdmin(admin.ModelAdmin):
    pass
