from django.shortcuts import get_object_or_404
from rest_framework.views import APIView , Response
from rest_framework import status

from .serializers import PostSerializer , PostUpdateSerializer

from .models import Post


class PostDetail(APIView):
    @staticmethod
    def get(request , id):
        post = get_object_or_404(Post , id=id)
        serializer = PostSerializer(post)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    def put(request , id):
        post = get_object_or_404(Post , id=id)
        serializer = PostUpdateSerializer(post , data=request.data , context={'request':request} , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        return  Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    @staticmethod
    def get(request):
        posts = Post.objects.all().order_by['-created']

