# urls.py
from django.urls import path
from .views import VideoListCreateView, VideoDetailAPIview

urlpatterns = [
    path('', VideoListCreateView.as_view(), name='videocreate'),
    path('videos/pk>/', VideoDetailAPIview.as_view(), name='video-detail'),
]

