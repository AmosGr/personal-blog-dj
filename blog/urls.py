from django.urls import path
from .views.post_view import PostView,post_detail

urlpatterns = [
    path("",PostView.as_view(), name="home"),
    path("<str:author>/<slug:slug>/", post_detail,name='post_detail'),
]