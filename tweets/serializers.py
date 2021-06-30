from rest_framework import serializers
from .models import Comments, Like, Retweet, Tweet
from rest_framework.serializers import ModelSerializer

class TweetSerializer(ModelSerializer):
    username = serializers.CharField(source = "user.username", read_only = True)
    likes = serializers.IntegerField(source = "get_num_of_likes", read_only = True)
    retweet = serializers.IntegerField(source = "get_num_of_retweets", read_only = True)
    comments = serializers.IntegerField(source = "get_num_of_comments", read_only = True)

    def to_representation(self, instance):
        data = super(TweetSerializer, self).to_representation(instance)
        data.update({"text":"yeah"})
        return data

    class Meta:
        model = Tweet
        fields = ["text", "user","username","likes","retweet","created_on","comments"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["tweet","user"]


class RetweetSerializer(ModelSerializer):
    
    class Meta:
        model = Retweet
        fields = ["tweet","user"]


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ["tweet","user"]