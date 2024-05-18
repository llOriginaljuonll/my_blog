from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True)
    slug = AutoSlugField(
        unique=True,
        max_length=100,
        populate_from="user",
    )
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user}'
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # Have the user follow themselves
        # ตั้งค่าให้เวลา User สมัครได้แล้วให้ทำการติดตามตัวเองโดยอัตโนมัติ
        user_profile.save()