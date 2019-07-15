from .serializers import UserSerializer,CustomLoginSerializer
from .models import CustomerUser
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import LoginView, LogoutView

class RegisterView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class CustomLogin(LoginView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer