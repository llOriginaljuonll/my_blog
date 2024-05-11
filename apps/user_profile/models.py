from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    slug = AutoSlugField(
        unique=True,
        max_length=100,
        populate_from="user",
    )
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.user}'