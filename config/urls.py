from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls', namespace='Users')),
    path('', include('Clubs.urls', namespace='Clubs')),
]
