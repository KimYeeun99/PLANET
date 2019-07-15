from rest_framework.serializers import ModelSerializer
from .models import CustomerUser
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(ModelSerializer,LoginSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username','password']

class UserSerializer(ModelSerializer,RegisterSerializer):
    class Meta:
        model = CustomerUser
        fields = ['email','username','password1','password2','name','nickname','gender','birth_date']