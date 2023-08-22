from django.urls import path
from .views import ListUser

urlpatterns = [
    path("hello", ListUser.as_view()),
]
