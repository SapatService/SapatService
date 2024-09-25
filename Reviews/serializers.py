from rest_framework import serializers
from .models import Review, OurTeam, GeoLocate, WhatsApp, Instagram, Telegram, TikTok

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'first_name', 'last_name', 'stars', 'text', "image"]

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'first_name', 'last_name', 'role', 'image']

class GeoLocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocate
        fields = ['id', 'map_image', 'locate', 'working_hours', 'map_url']

class WhatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsApp
        fields = ['id', 'url']

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = ['id', 'url']

class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telegram
        fields = ['id', 'url']

class TikTokSerializer(serializers.ModelSerializer):
    class Meta:
        model = TikTok
        fields = ['id', 'url']
