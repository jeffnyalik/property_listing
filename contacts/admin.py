from django.contrib import admin
from contacts.models.contact_model import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject']

admin.site.register(Contacts, ContactsAdmin)