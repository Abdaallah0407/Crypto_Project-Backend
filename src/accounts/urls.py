from django.urls import path, include
from src.accounts.views import UserAPI

urlpatterns = [
    path('api/auth/user', UserAPI.as_view()),
]
