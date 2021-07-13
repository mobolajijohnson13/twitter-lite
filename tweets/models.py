from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Tweet(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_num_of_likes(self):
        return Like.objects.filter(tweet=self).count()
    
    def get_num_of_retweets(self):
        return Retweet.objects.filter(tweet=self).count()
    
    def get_num_of_comments(self):
        return Comments.objects.filter(tweet=self).count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "tweet"]


class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "tweet"]


class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete= models.CASCADE)
    

    class Meta:
        unique_together = ["user", "text"]
    



