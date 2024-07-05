from django.contrib import admin
from django.urls import path, include
import user
import tweet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('profile/', include('tweet.urls')),
]
