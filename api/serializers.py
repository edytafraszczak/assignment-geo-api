from rest_framework import serializers

from api.models import GeoLocation


class GeoLocationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = ['ip', 'type', 'continent_code', 'continent_name', 'country_code', 'country_name', 'region_code',
                  'city', 'zip', 'latitude', 'longitude']


class GeoLocationFetchSerializer(GeoLocationReadSerializer):
    class Meta:
        model = GeoLocation
        fields = '__all__'
