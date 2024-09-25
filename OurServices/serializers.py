from rest_framework import serializers
from .models import OurService, OurServiceDetail, OurServicePrice

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = ['id', 'title', 'ImageOurService']

class OurServiceDetailSerializer(serializers.ModelSerializer):
    our_service = OurServiceSerializer(read_only=True)

    class Meta:
        model = OurServiceDetail
        fields = ['id', 'our_service', 'title', 'ImageDetailOurService']

class OurServicePriceSerializer(serializers.ModelSerializer):
    our_service = OurServiceDetailSerializer(read_only=True)

    class Meta:
        model = OurServicePrice
        fields = ['id', 'our_service', 'price', 'contact']
