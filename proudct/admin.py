from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Brand,Category,ProudctImge,ProudctReview,Proudct,Test
# Register your models here.

# adding image in Porudct
class ProudctImgeInline(admin.TabularInline):
    model=ProudctImge 

# smarnote
class ProudctModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines=[ProudctImgeInline]



admin.site.register(Proudct,ProudctModelAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProudctImge)
admin.site.register(ProudctReview)
admin.site.register(Test)

