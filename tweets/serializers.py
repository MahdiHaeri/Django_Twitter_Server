from rest_framework import serializers
from tweets.models import Tweet, Retweet


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
        model = Tweet
        fields = '__all__'


class QuoteTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
