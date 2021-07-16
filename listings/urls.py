from django.urls import path
from listings.views.listings import (
    ListingView, ListingsApiView, SearchApiView
)

urlpatterns = [
    path('listings/', ListingsApiView.as_view(), name='listings'),
    path('listings/search', SearchApiView.as_view(), name='search'),
    path('listings/<slug>', ListingView.as_view(), name='listing-view')
]