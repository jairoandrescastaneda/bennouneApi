from rest_framework import serializers
from users.models import CustomUser
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ()