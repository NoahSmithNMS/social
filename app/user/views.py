"""
Views for the User API.
"""
from rest_framework import generics, authentication, permissions, status
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.conf import settings

from user.serializers import (
    UserSerializer,
    LoginSerializer,
)

from . import views


def home(request):
    return render(request, 'authentication/index.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        # Handle the form submission
        pass
    else:
        # Render the registration form
        return render(request, 'register.html', {'request_data': request.GET})

"""
CSRF Authentication
"""
class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


"""
Login User
"""
class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        return Response(UserSerializer(user).data)

"""
Logout User
"""
class LogoutView(views.APIView):
    def post(self, request):
        django_logout(request)
        return Response()

"""
Register new User
"""
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        django_login(self.request, user)

"""
Retreive User Data
"""
class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user