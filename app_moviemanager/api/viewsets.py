from rest_framework import viewsets
from app_moviemanager.api import serializers
from app_moviemanager import models

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MoviesSerializer
    queryset = models.Movies.objects.all()