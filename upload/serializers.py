from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('large', 'url'),
            ('thumbnail', 'thumbnail__200x300'),
            ('medium', 'crop__500x500'),
            ('small', 'crop__50x50'),
            ('grayscale', 'filters__invert__url'),
        ]
    )

    class Meta:
        model = Photo
        fields = (
            'user',
            'image',
 
        )