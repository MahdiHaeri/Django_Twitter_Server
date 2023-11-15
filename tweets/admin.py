from django.contrib import admin

from tweets.models import Tweet, Retweet, ReplyTweet, QuoteTweet, Like


# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'tweet_type', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


class RetweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'tweet_type', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'retweet')


class ReplyTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'tweet_type', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'reply')


class QuoteTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'tweet_type', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'quote')


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'tweet', 'created_at', 'updated_at')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Retweet, RetweetAdmin)
admin.site.register(ReplyTweet, ReplyTweetAdmin)
admin.site.register(QuoteTweet, QuoteTweetAdmin)
admin.site.register(Like, LikeAdmin)
