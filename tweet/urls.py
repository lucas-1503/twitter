from django.urls import path
from . import views

urlpatterns = [
    path('send_tweet', views.send_tweet, name='send_tweet'),
    path('tweet/<int:pk>/delete/', views.delete_tweet, name='delete_tweet'),
    path('tweet/<int:pk>/update/', views.tweet_update, name='update_tweet'),
]
