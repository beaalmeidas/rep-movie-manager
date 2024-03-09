from rest_framework import viewsets
from app_moviemanager.api import serializers
from app_moviemanager import models
import requests
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ViewSet que lida com buscar os filmes (GET)
# list(): mostra todos os filmes já avaliados e cadastrados no banco de dados
# retrieve(): mostra um filme buscado pela API do OMDb
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


# ViewSet que lida com as funções POST, PUT, DELETE
# - create(): a variável 'titulo' é usada para associar os valores 'nota_create' e 'comentario_create' 
# aos campos 'nota' e 'comentario'. Além disso, os outros campos componentes do model são buscados na API
# - update(): atualiza as variáveis 'nota' e 'comentario' com os valores novos em 'nota_update' e 'comentario_update'
# - destroy(): deleta o objeto
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

        return Response("Avaliação atualizada")
    
    def destroy(self, request, pk=None):
        obj = self.get_object()
        obj.delete()
        return Response("Avaliação excluída")