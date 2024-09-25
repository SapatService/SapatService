from django.urls import path
from .views import *


urlpatterns = [
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus-list-create'),
    path('about-us/<int:pk>/', AboutUsViewSet.as_view({'get': 'retrieve'}), name='aboutus-detail'),

    path('about-our-experience/', AboutOurExperienceViewSet.as_view({'get': 'list'}), name='about-our-experience-list'),
    path('about-our-experience/<int:pk>/', AboutOurExperienceViewSet.as_view({'get': 'retrieve'}), name='about-our-experience-detail'),
]
