from django.db import models
from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey( CustomUser , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.author.email + self.title