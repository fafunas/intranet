from rest_framework import routers,serializers,viewsets

from .models import noticia, documento, rol, training

class NotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = noticia
        fields = '__all__'

class DocumentSerializer( serializers.ModelSerializer):
    class Meta:
        model = documento
        fields = '__all__'

class RolSerializer( serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'

class TrainingSerializer ( serializers.ModelSerializer):
    class Meta:
        model = training
        fields = '__all__'