from django.urls import path
from .views import OurServiceViewSet, OurServiceDetailViewSet, OurServicePriceViewSet

urlpatterns = [
    path('our-services/', OurServiceViewSet.as_view({'get': 'list'}), name='ourservice-list-create'),
    path('our-services/<int:pk>/', OurServiceViewSet.as_view({'get': 'retrieve'}), name='ourservice-detail'),

    path('our-service-details/', OurServiceDetailViewSet.as_view({'get': 'list'}), name='ourservicedetail-list-create'),
    path('our-service-details/<int:pk>/', OurServiceDetailViewSet.as_view({'get': 'retrieve'}), name='ourservicedetail-detail'),

    path('our-service-prices/', OurServicePriceViewSet.as_view({'get': 'list'}), name='ourserviceprice-list-create'),
    path('our-service-prices/<int:pk>/', OurServicePriceViewSet.as_view({'get': 'retrieve'}), name='ourserviceprice-detail'),
]
