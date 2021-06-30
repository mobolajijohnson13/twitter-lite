from django.contrib import admin
from tweets.models import Like, Retweet, Tweet
from django.contrib import admin
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Retweet)