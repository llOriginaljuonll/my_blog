from django.urls import path
from .views import profile_detail

urlpatterns = [
    path('<slug:slug>/', profile_detail, name='user_profile'),
]
