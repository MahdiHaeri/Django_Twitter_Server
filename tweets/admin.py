from django.contrib import admin

from tweets.models import Tweet, Retweet, ReplyTweet, QuoteTweet, Like


# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at')


class RetweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'retweet_id')


class ReplyTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'reply_id')


class QuoteTweetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'content', 'replyCount', 'retweetCount', 'likeCount',
        'created_at', 'updated_at', 'quote_id')


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_id', 'tweet_id', 'created_at', 'updated_at')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Retweet, RetweetAdmin)
admin.site.register(ReplyTweet, ReplyTweetAdmin)
admin.site.register(QuoteTweet, QuoteTweetAdmin)
admin.site.register(Like, LikeAdmin)
