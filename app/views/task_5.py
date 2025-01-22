from rest_framework import viewsets
from app.models import User
from app.serializers import UserSerializer
from django.urls import path, include
from rest_framework.routers import DefaultRouter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = DefaultRouter()
router.register("users", UserViewSet)
