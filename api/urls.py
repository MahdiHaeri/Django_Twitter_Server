from django.urls import path, include
from tweets import views as tweets_views
from users import views as users_views

urlpatterns = [
    path('users/', include("users.urls")),
    path('tweets/', include("tweets.urls")),
]
