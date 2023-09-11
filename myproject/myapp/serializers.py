from rest_framework import serializers
from myapp.models import HomeDescription



class HomeDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomeDescription
        fields=['id','heading','banner_image_url']