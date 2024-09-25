from django.contrib import admin
from .models import Review, OurTeam, GeoLocate, WhatsApp, Instagram, Telegram, TikTok

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'stars', 'text')
    search_fields = ('first_name', 'last_name', 'stars')
    list_filter = ('stars',)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    search_fields = ('first_name', 'last_name', 'role')

@admin.register(GeoLocate)
class GeoLocateAdmin(admin.ModelAdmin):
    list_display = ('locate', 'working_hours')
    search_fields = ('locate',)

@admin.register(WhatsApp)
class WhatsAppAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)

@admin.register(TikTok)
class TikTokAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)
