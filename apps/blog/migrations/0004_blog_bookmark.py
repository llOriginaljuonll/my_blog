# Generated by Django 5.0.1 on 2024-05-26 11:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bookmark',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarked', to=settings.AUTH_USER_MODEL),
        ),
    ]
