from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import DocumentoViewSet, NoticiaViewSet, RolViewSet

router = routers.DefaultRouter()
router.register(r'docs',DocumentoViewSet)
router.register(r'rol',RolViewSet)
router.register(r'news',NoticiaViewSet)

urlpatterns = [
    path('',include(router.urls))
]
