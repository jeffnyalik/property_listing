from contacts.models.contact_model import Contacts
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contacts