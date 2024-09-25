from rest_framework import viewsets
from .models import OurService, OurServiceDetail, OurServicePrice
from .serializers import OurServiceSerializer, OurServiceDetailSerializer, OurServicePriceSerializer

class OurServiceViewSet(viewsets.ModelViewSet):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer

class OurServiceDetailViewSet(viewsets.ModelViewSet):
    queryset = OurServiceDetail.objects.all()
    serializer_class = OurServiceDetailSerializer

class OurServicePriceViewSet(viewsets.ModelViewSet):
    queryset = OurServicePrice.objects.all()
    serializer_class = OurServicePriceSerializer
