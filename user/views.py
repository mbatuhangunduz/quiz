from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, serializers
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()


