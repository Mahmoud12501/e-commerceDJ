from django.contrib import admin
from .models import Profile,ContactNumbers,DeliveryAddress
# Register your models here.
class ContactNumbersInline(admin.TabularInline):
    model=ContactNumbers

class DeliveryAddressInline(admin.TabularInline):
    model=DeliveryAddress

class ProfileModelAdmin(admin.ModelAdmin):
    inlines=[ContactNumbersInline,DeliveryAddressInline]

admin.site.register(Profile,ProfileModelAdmin)
admin.site.register(ContactNumbers)
admin.site.register(DeliveryAddress)

