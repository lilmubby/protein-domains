from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterUserSerializer
from rest_framework import generics, permissions


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterUserSerializer
