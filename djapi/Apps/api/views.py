from re import I
from django.shortcuts import render
from rest_framework import viewsets
from .models import documento, rol, noticia
from .serializer import DocumentSerializer, NotiSerializer,RolSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = documento.objects.all().order_by('id')
    serializer_class = DocumentSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all().order_by('id')
    serializer_class = RolSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = noticia.objects.all().order_by('id')
    serializer_class = NotiSerializer