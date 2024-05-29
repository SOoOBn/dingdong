from django.urls import path
from .views import ClubAPIView, ClubListAPIView

app_name = 'Clubs'

urlpatterns = [
    path('clubs/register/', ClubAPIView.as_view()),
    path('allclubs/', ClubListAPIView.as_view())
]