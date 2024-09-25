from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ['id', 'image', 'description']

    def get_image(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(image.image.url) for image in obj.images.all()]


class AboutOurExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutOurExperience
        fields = '__all__'
