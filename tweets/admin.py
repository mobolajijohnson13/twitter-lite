from django.contrib import admin
from tweets.models import Comments, Like, Retweet, Tweet
from django.contrib import admin
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Retweet)
admin.site.register(Comments)