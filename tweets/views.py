from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tweets.models import Tweet, Retweet, ReplyTweet, QuoteTweet
from tweets.serializers import TweetSerializer, RetweetSerializer, ReplyTweetSerializer, QuoteTweetSerializer


class TweetView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class TweetDetailsView(APIView):
    def get(self, request, tweet_id):
        try:
            tweet = Tweet.objects.get(id=tweet_id)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        except Tweet.DoesNotExist:
            return Response({"message": "tweet not found"}, status=status.HTTP_404_NOT_FOUND)


class RetweetView(APIView):
    def get(self, request):
        retweets = Retweet.objects.all()
        serializer = RetweetSerializer(retweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RetweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class RetweetDetailsView(APIView):
    def get(self, request, tweet_id):
        try:
            retweet = Retweet.objects.get(id=tweet_id)
            serializer = TweetSerializer(retweet)
            return Response(serializer.data)
        except Retweet.DoesNotExist:
            return Response({"message": "tweet not found"}, status=status.HTTP_404_NOT_FOUND)


class ReplyTweetView(APIView):
    def get(self, request):
        reply_tweets = ReplyTweet.objects.all()
        serializer = ReplyTweetSerializer(reply_tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplyTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ReplyTweetDetailsView(APIView):
    def get(self, request, tweet_id):
        try:
            reply_tweet = ReplyTweet.objects.get(id=tweet_id)
            serializer = ReplyTweetSerializer(reply_tweet)
            return Response(serializer.data)
        except ReplyTweet.DoesNotExist:
            return Response({"message": "tweet not found"}, status=status.HTTP_404_NOT_FOUND)


class QuoteTweetView(APIView):
    def get(self, request):
        quote_tweets = QuoteTweet.objects.all()
        serializer = QuoteTweetSerializer(quote_tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class QuoteTweetDetailsView(APIView):
    def get(self, request, tweet_id):
        try:
            quote_tweet = QuoteTweet.objects.get(id=tweet_id)
            serializer = QuoteTweetSerializer(quote_tweet)
            return Response(serializer.data)
        except QuoteTweet.DoesNotExist:
            return Response({"message": "tweet not found"}, status=status.HTTP_404_NOT_FOUND)
