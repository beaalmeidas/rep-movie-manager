from rest_framework import viewsets
from app_moviemanager.api import serializers
from app_moviemanager import models
import requests
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MoviesSerializer
    queryset = models.Movies.objects.all()

    def create(self, request):
        response = requests.get(api_url)
        print(response.json())

    def list(self, request):
        titulo = request.query_params.get("nome")
        api_url = f'http://www.omdbapi.com/?t={titulo}&type=movie&apikey=1487ead9&'
        response = requests.get(api_url)
        return Response(response.json())

    def retrieve(self, request, pk=None):
        titulo = request.query_params.get("nome")
        api_url = f'http://www.omdbapi.com/?t={titulo}&type=movie&apikey=1487ead9&'
        response = requests.get(api_url)
        return Response(response.json())
