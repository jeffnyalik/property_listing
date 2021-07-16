from django.contrib import admin
from realtors.models import Realtors


class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date_hired']
    list_display_links = ['id', 'name']
    search_fields = ['id','name']


admin.site.register(Realtors, RealtorAdmin)