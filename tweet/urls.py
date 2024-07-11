from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.profile_view, name='profile' ),
    path('send_tweet', views.send_tweet, name='send_tweet'),
    path('tweet/<int:pk>/delete/', views.delete_tweet, name='delete_tweet'),
    path('feed/<int:pk>', views.feed_view, name='feed')
]
