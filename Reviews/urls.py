from django.urls import path
from .views import (
    ReviewViewSet, OurTeamViewSet, GeoLocateViewSet,
    WhatsAppViewSet, InstagramViewSet, TelegramViewSet, TikTokViewSet
)

urlpatterns = [
    path('reviews/', ReviewViewSet.as_view({'get': 'list'}), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'}), name='review-detail'),

    path('our-team/', OurTeamViewSet.as_view({'get': 'list'}), name='ourteam-list-create'),
    path('our-team/<int:pk>/', OurTeamViewSet.as_view({'get': 'retrieve'}), name='ourteam-detail'),

    path('geo-locate/', GeoLocateViewSet.as_view({'get': 'list'}), name='geolocate-list-create'),
    path('geo-locate/<int:pk>/', GeoLocateViewSet.as_view({'get': 'retrieve'}), name='geolocate-detail'),

    path('whatsapp/', WhatsAppViewSet.as_view({'get': 'list'}), name='whatsapp-list-create'),
    path('instagram/', InstagramViewSet.as_view({'get': 'list'}), name='instagram-list-create'),
    path('telegram/', TelegramViewSet.as_view({'get': 'list'}), name='telegram-list-create'),
    path('tiktok/', TikTokViewSet.as_view({'get': 'list'}), name='tiktok-list-create'),
]
