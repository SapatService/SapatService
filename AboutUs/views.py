from rest_framework import viewsets
from .models import *
from .serializers import *


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutOurExperienceViewSet(viewsets.ModelViewSet):
    queryset = AboutOurExperience.objects.all()
    serializer_class = AboutOurExperienceSerializer
