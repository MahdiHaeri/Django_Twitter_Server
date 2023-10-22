from django.contrib import admin

from tweets.models import Tweet, Retweet, ReplyTweet, QuoteTweet


# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


class RetweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


class ReplyTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


class QuoteTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(ReplyTweet)
admin.site.register(QuoteTweet)
