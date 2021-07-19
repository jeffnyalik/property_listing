from django.urls import path

from .import views

urlpatterns = [
    path('contacts', views.ContactApiView.as_view(), name='contacts')
]