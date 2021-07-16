from django.urls import path
from realtors.views.realtor_view import (
    RealtorView, RealtorsListView, TopRealtorApiView
)

urlpatterns = [
    path('realtors/', RealtorsListView.as_view(), name='list-realtors'),
    path('realtors/<pk>/', RealtorView.as_view(), name='realtor'),
    path('realtors/top-seller', TopRealtorApiView.as_view(), name='top-seller')
]