# Create your views here.
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from api.models import GeoLocation
from api.serializers import GeoLocationFetchSerializer, GeoLocationReadSerializer
from api.utils import fetch_ip_details


class ReadOnlyOrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff


class RetrieveGeoLocation(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    request_lookup_field = 'ip_or_url'
    model_lookup_field = 'ip_or_url'
    queryset = GeoLocation.objects.all()

    serializer_method_map = {"POST": GeoLocationFetchSerializer}
    serializer_class = GeoLocationReadSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrStaff, ]

    def get_serializer_class(self):
        return self.serializer_method_map.get(self.request.method, super().get_serializer_class())

    def get_object(self):
        location = None
        ip_or_url = self.request.query_params.get(self.request_lookup_field, None)
        if ip_or_url:
            try:
                location = self.queryset.get(**{self.model_lookup_field: ip_or_url})
            except:
                remote_location = fetch_ip_details(ip_or_url)
                if remote_location:
                    remote_location[self.model_lookup_field] = ip_or_url
                    serialized_location = GeoLocationFetchSerializer(data=remote_location)
                    if serialized_location.is_valid():
                        location = GeoLocation.objects.create(**serialized_location.validated_data)
        if location:
            self.check_object_permissions(self.request, location)
            return location
        else:
            raise NotFound()
