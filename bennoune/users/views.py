from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from users.serializers import UserSignupSerializer , UserSerializer , UserLoginSerializer

from users.models import CustomUser


class UserList(APIView):
    @staticmethod
    def get(request):
        users = CustomUser.objects.all()
        serializers = UserSerializer(users,many=True)
        return Response(data = serializers.data , status = status.HTTP_200_OK)

class UserDetail(APIView):
    @staticmethod
    def get(request, id):
        user = get_object_or_404(CustomUser , id=id)
        if user :
            serializer = UserSerializer(user)
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    @staticmethod
    def put(request , id):
        user = get_object_or_404(CustomUser , id=id)
        if user : 
            user.first_name = request.data.get('first_name')
            user.last_name = request.data.get('last_name')
            user.save()
            serializer = UserSerializer(user)
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserSignupAPIView(APIView):
    @staticmethod
    def post(request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(data=serializer.data , status=status.HTTP_201_CREATED   )
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)

        
        
class UserLoginAPIView(APIView):
    @staticmethod
    def post(request):
        user = get_object_or_404(CustomUser , email = request.data.get('email'))
        user = authenticate(email = user.email , password = request.data.get('password'))
        if user : 
            serializer = UserLoginSerializer(user)
            return Response(serializer.data , status =status.HTTP_201_CREATED) 
        return Response()


class UserLogout(APIView):
    @staticmethod 
    def post(request):
        if is_authenticated(request.user):
            token = Token.get_object_or_404(Token , key=request.auth)
        return Response(status=status.HTTP_200_OK)

