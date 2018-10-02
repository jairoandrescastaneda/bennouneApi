from django.contrib.auth import authenticate
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","email" , "first_name" , "last_name" , "password" , "is_active" )

    
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email" , "first_name" , "last_name" , "password" )

    
        
class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    
    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

    
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name','token')

