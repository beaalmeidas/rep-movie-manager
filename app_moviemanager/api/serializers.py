from rest_framework import serializers
from app_moviemanager import models

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'