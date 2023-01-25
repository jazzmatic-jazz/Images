from django.shortcuts import render
from .models import Photo
from .serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet

class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()