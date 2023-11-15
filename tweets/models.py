from django.db import models


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    replyCount = models.IntegerField()
    retweetCount = models.IntegerField()
    likeCount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Retweet(Tweet):
    retweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='retweets')

    def __str__(self):
        return self.content


class ReplyTweet(Tweet):
    reply = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.content


class QuoteTweet(Tweet):
    quote = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.content


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
