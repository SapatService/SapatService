from rest_framework import viewsets
from .models import Review, OurTeam, GeoLocate, WhatsApp, Instagram, Telegram, TikTok
from .serializers import (
    ReviewSerializer, OurTeamSerializer, GeoLocateSerializer,
    WhatsAppSerializer, InstagramSerializer, TelegramSerializer, TikTokSerializer
)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer

class GeoLocateViewSet(viewsets.ModelViewSet):
    queryset = GeoLocate.objects.all()
    serializer_class = GeoLocateSerializer

class WhatsAppViewSet(viewsets.ModelViewSet):
    queryset = WhatsApp.objects.all()
    serializer_class = WhatsAppSerializer

class InstagramViewSet(viewsets.ModelViewSet):
    queryset = Instagram.objects.all()
    serializer_class = InstagramSerializer

class TelegramViewSet(viewsets.ModelViewSet):
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializer

class TikTokViewSet(viewsets.ModelViewSet):
    queryset = TikTok.objects.all()
    serializer_class = TikTokSerializer
