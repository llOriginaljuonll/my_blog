from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    name = models.CharField(max_length=255)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='Blog_like', blank=True)
    bookmark = models.ManyToManyField(User, related_name='bookmarked', default=None, blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.name}'