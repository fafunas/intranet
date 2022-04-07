from django.shortcuts import render
from rest_framework import viewsets
from .models import documento, rol, noticia
from .serializer import DocumentSerializer, NotiSerializer,RolSerializer

# Create your views here.

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = documento.objects.all().order_by('id')
    serializer_class = DocumentSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all().order_by('id')
    serializer_class = RolSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = noticia.objects.all().order_by('id')
    serializer_class = NotiSerializer