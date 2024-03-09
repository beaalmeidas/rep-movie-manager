from rest_framework import viewsets
from app_moviemanager.api import serializers
from app_moviemanager import models
import requests
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MoviesViewSet(viewsets.ModelViewSet):

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


class AnalysisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovieAnalysisSerializer
    queryset = models.MovieAnalysis.objects.all()
