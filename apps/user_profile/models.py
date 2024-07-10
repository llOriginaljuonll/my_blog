from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.dispatch import receiver
from datetime import date

from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = VersatileImageField(
        'Image',
        upload_to='images',
        null=True
    )
    slug = AutoSlugField(
        unique=True,
        max_length=100,
        populate_from="user",
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    birthdate = models.DateField(null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}'
    
    def calculate_age(self):
        today = date.today()
        if self.birthdate:
            user_age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            return user_age
        
    def save(self, *args, **kwargs):
        if not self.age or self.age:
            self.age = self.calculate_age()

        super().save(*args, **kwargs)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # Have the user follow themselves
        # ตั้งค่าให้เวลา User สมัครได้แล้วให้ทำการติดตามตัวเองโดยอัตโนมัติ
        user_profile.save()