from datetime import date
from rest_framework import routers,serializers,viewsets

from .models import noticia, documento, rol, training

class NotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = noticia
        fields = ['id','name','description','image','shortDescription','update']

class DocumentSerializer( serializers.ModelSerializer):
    
    class Meta:
        model = documento
        fields = ['id','name','description','file','rolId']

class RolSerializer( serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'

class TrainingSerializer ( serializers.ModelSerializer):
    class Meta:
        model = training
        fields = '__all__'