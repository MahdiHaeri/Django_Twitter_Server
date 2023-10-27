from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tweets.models import Tweet
from tweets.serializers import TweetSerializer


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
