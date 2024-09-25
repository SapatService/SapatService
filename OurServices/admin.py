from django.contrib import admin
from .models import OurService, OurServiceDetail, OurServicePrice


@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(OurServiceDetail)
class OurServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('our_service', 'title')
    search_fields = ('our_service__title', 'title')

@admin.register(OurServicePrice)
class OurServicePriceAdmin(admin.ModelAdmin):
    list_display = ('our_service', 'price')
    search_fields = ('our_service__our_service__title',)
