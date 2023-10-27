from django.urls import path
from tweets import views

urlpatterns = [
    path('', views.TweetView.as_view()),
    path('<int:tweet_id>/', views.TweetDetailsView.as_view()),
]
