from rest_framework import serializers
from users.models import CustomUser
from posts.models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('title' , 'content' , 'author')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta :
        fields = ('title' , 'content')


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta :
        fields = ('title' , 'content')

    def validate(self, data):
        if self.instance.author != self.context['request'].user:
            return serializers.ValidationError('Unable to update this post')
        return data
