from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    path('<slug:slug>/', ProfileDetailView.as_view(), name='user_profile'),
]
