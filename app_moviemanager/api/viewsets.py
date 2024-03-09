from rest_framework import viewsets
from app_moviemanager.api import serializers
from app_moviemanager import models
import requests
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovieAnalysisSerializer
    queryset = models.MovieAnalysis.objects.all()

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

    def create(self, request):
        titulo = request.data.get("nome")
        nota_create = request.data.get("nota")
        comentario_create = request.data.get("comentario")

        api_url = f'http://www.omdbapi.com/?t={titulo}&type=movie&apikey=1487ead9&'
        response = requests.get(api_url)
        data = response.json()

        nome_create = data.get('Title', '')
        lancamento_create = data.get('Year', '')
        diretor_create = data.get('Director', '')
        sinopse_create = data.get('Plot', '')

        review_database = models.MovieAnalysis(nome=nome_create, lancamento=lancamento_create, diretor=diretor_create, sinopse=sinopse_create, nota=nota_create, comentario=comentario_create)
        review_database.save()
        return Response("Avaliação enviada")
    
    def update(self, request, pk=None):
        nota_update = titulo = request.data.get("nota atualizada")
        comentario_update = titulo = request.data.get("comentario atualizado")
        
        obj = self.get_object()
        obj.nota = nota_update
        obj.comentario= comentario_update
        obj.save()

        return Response("Comentário atualizado")
    
    def destroy(self, request, pk=None):
        obj = self.get_object()
        obj.delete()
        return Response("Avaliação excluída")
        