"""
Views for the User API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from django.http import HttpResponse
from django.shortcuts import render

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


def home(request):
    return render(request, 'authentication/index.html')


def signup(request):
    return render(request, 'authentication/signup.html')


def login(request):
    return render(request, 'authentication/login.html')


def logout(request):
    pass


# CreateAPIView handles HTTP POST request
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateAuthTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user
