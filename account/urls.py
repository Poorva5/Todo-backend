from django.urls import path
from .views import UserCreate

urlpatterns = [
    path("auth/create/", UserCreate.as_view()),
]