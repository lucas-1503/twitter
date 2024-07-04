from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.home_view, name='profile' ),
]
