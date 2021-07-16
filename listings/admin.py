from django.contrib import admin
from listings.models import Listings

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['realtor']
    list_display_links =['id', 'title']
    search_fields = ['title', 'description', 'city', 'address', 'town']

admin.site.register(Listings, ListingAdmin)