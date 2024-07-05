from django.urls import path, include
from . import views
from .views import login_view

urlpatterns = [
    path('', views.login_view, name='home' ),
]
