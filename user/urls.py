from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
    path('', views.login_view, name='home' ),
    path('register', views.register_view, name='register'),
    path('detail/', views.detail_view, name='detail'),
    path('', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('<int:pk>/', views.profile_view, name='profile' ),
    path('detail', views.alterar_avatar, name='alterar_avatar'),
    path('follow/<int:pk>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:pk>/', views.unfollow_user, name='unfollow_user'),
    path('user_list/<int:pk>/', views.user_list, name='user-list')
]
