"""
URL configuration for project_moviemanager project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_moviemanager.api import viewsets as moviesviewsets


route = routers.DefaultRouter()
route.register(r'movies', moviesviewsets.MoviesViewSet, basename="Movies")
route.register(r'review', moviesviewsets.AnalysisViewSet, basename="Reviews")
# - 'movies': rota utilizada para mostrar as informações de um filme buscado pelo parâmetro 'nome' (teste da função retrieve)
# - 'review': rota utilizada para os testes das funções list, create, update e destroy, associada ao Id do filme
# no banco de dados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]