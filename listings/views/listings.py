from django.shortcuts import render
from listings.models import Listings
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from serializers.listings.listings_serializer import ListingSerializers
from rest_framework.response import Response
from rest_framework import status


class ListingsApiView(ListAPIView):
    queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializers
    lookup_field = 'slug'


class ListingView(RetrieveAPIView):
    queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializers
    lookup_field = 'slug'


class SearchApiView(APIView):
    serializer_class = ListingSerializers

    def post(self, request, format=None):
        queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data
        sale_type = data['sale_type']
        town = data['town']
        city = data['city']
        home_type = data['home_type']
    

        queryset = queryset.filter(sale_type__iexact=sale_type)
        queryset = queryset.filter(home_type__iexact=home_type)
        queryset = queryset.filter(town__iexact=town)
        queryset = queryset.filter(city__iexact=city)
        
        serializer = ListingSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
        
