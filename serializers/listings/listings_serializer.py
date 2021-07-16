from rest_framework import serializers
from listings.models import Listings

class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'