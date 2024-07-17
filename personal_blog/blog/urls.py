from django.urls import path
from .views.views import welcome

urlpatterns = [
    path("", welcome, name="welcome")
    ]