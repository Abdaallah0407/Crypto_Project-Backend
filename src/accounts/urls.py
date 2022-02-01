from django.urls import path, include
from src.accounts.views import UserAPI

urlpatterns = [
    path('api/user/', UserAPI.as_view()),
]
