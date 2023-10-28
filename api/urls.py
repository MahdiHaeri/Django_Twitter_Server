from django.urls import path, include
from tweets import views as tweets_views
from users import views as users_views

urlpatterns = [
    path('', include("users.urls")),
    path('', include("tweets.urls")),
    path('profiles/', include("profiles.urls")),
]
