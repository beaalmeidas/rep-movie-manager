from rest_framework import serializers
from app_moviemanager import models


# Serializer que busca todos os campos do objeto
class MovieAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieAnalysis
        fields = '__all__'