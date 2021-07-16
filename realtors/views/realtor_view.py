from django.shortcuts import render
from realtors.models.realtor import Realtors
from serializers.realtors.realtor_serializers import RealtorSerialzer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework import permissions


class RealtorsListView(ListAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerialzer

class RealtorView(RetrieveAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerialzer

class TopRealtorApiView(ListAPIView):
    queryset = Realtors.objects.filter(top_seller=True)
    serializer_class = RealtorSerialzer
    