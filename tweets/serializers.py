from .models import Like, Retweet, Tweet
from rest_framework.serializers import ModelSerializer

class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["text", "user"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class RetweetSerializer(ModelSerializer):
    class Meta:
        model = Retweet
        fields = "__all__"