from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.profile_view, name='profile' ),
    path('send_tweet', views.send_tweet, name='send_tweet')
]
