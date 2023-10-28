from rest_framework import serializers
from tweets.models import Tweet, Retweet, ReplyTweet, QuoteTweet, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retweet
        fields = '__all__'


class ReplyTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyTweet
        fields = '__all__'


class QuoteTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteTweet
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
