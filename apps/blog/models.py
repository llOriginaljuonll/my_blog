from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    blog_name = models.CharField(max_length=255)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.blog_name}'