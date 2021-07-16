from rest_framework import serializers
from realtors.models.realtor import Realtors


class RealtorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Realtors
        fields = ['id', 'name', 'phone', 'email', 'image', 'top_seller']