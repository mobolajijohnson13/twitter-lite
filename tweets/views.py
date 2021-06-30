from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from tweets.serializers import LikeSerializer, RetweetSerializer, TweetSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Like, Retweet, Tweet

# Create your views here.


def tone(request):
    return HttpResponse("Hello Liberty")


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RetweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Retweet.objects.all()
    serializer_class = RetweetSerializer
    # permission_classes = [permissions.IsAuthenticated]
