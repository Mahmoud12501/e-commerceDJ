from django.contrib import admin
from .models import Brand,Category,ProudctImge,ProudctReview,Proudct
# Register your models here.


class ProudctImgeInline(admin.TabularInline):
    model=ProudctImge 


class ProudctAdmin(admin.ModelAdmin):
    
    inlines=[ProudctImgeInline]






admin.site.register(Proudct,ProudctAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProudctImge)
admin.site.register(ProudctReview)
