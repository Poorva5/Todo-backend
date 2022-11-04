from django.urls import path
from .views import TaskList

urlpatterns = [
    path("create/", TaskList.as_view()),
    path("list/", TaskList.as_view()),
    path('edit/<str:id>/', TaskList.as_view()),
    path('delete/<str:id>/', TaskList.as_view())
]