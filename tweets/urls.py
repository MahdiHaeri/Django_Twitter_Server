from django.urls import path
from tweets import views

urlpatterns = [
    path('tweets/', views.TweetView.as_view()),
    path('tweets/<int:tweet_id>/', views.TweetDetailsView.as_view()),

    path('retweets/', views.RetweetView.as_view()),
    path('retweets/<int:tweet_id>/', views.RetweetDetailsView.as_view()),

    path('reply_tweets/', views.ReplyTweetView.as_view()),
    path('reply_tweets/<int:tweet_id>/', views.ReplyTweetDetailsView.as_view()),

    path('quote_tweets/', views.QuoteTweetView.as_view()),
    path('quote_tweets/<int:tweet_id>/', views.QuoteTweetDetailsView.as_view()),

    path('likes/', views.LikeView.as_view()),
    path('likes/<int:tweet_id>/', views.LikeDetailsView.as_view()),
]
