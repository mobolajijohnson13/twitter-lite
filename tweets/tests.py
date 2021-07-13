from typing import Text
from django.db.models.fields import TextField
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Comments, Tweet
from django.db import models


class TweetTests(APITestCase):
#     def test_create_tweet(self):
#         """
#         Ensure we can create a new tweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")

#         url = reverse('tweet-list')
#         data = {'text': 'DabApps', "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print()

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Tweet.objects.count(), 1)
#         self.assertEqual(Tweet.objects.get().text, data['text'])
#         self.assertEqual(response_data['text'], data['text'])

    # def test_get_tweet(self):
    #         """
    #         Ensure we can create a new tweet object.
    #         """
        
    #         user_instance = User.objects.create_user(username="lami", password="password123")#this is admin that create the tweet
    #         tweet =Tweet.objects.create(text="this is a simple tweet", user=user_instance)#this is admin that create the tweet

    #         url = reverse('tweet-detail', kwargs={'pk': tweet.id})
    #         response = self.client.get(url)
    #         response_data = response.json()
    #         # print()

    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(Tweet.objects.count(), 1)
    #         self.assertEqual(response_data['text'], tweet.text)


    def test_get_one_tweet(self):
                """
                Ensure we can create a new tweet object.
                """
            
                user_instance = User.objects.create_user(username="lami", password="password123")#this is admin that create the tweet
                tweet =Tweet.objects.create(text="this is a simple tweet", user=user_instance)#this is admin that create the tweet

                url = reverse('tweet-list')
                response = self.client.get(url)
                response_data = response.json()
                # print()

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(Tweet.objects.count(), 1)
                self.assertEqual(response_data[0]['text'],tweet.text)


#     def test_put_tweet(self):
#         """
#         Ensure we can create a new tweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")
#         tweet =Tweet.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('tweet-detail',kwargs={'pk': tweet.id})
#         data = {'text': 'DabApps', "user": user.id}
#         response = self.client.put(url, data, format='json')
#         response_data = response.json()
#         print()

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # self.assertEqual(Tweet.objects.count(), 1)
#         # self.assertEqual(Tweet.objects.put().text, data['text'])
#         # self.assertEqual(response_data['text'], data['text'])
     

# class RetweetTests(APITestCase):
#     def test_create_retweet(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('retweet-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class LikeTests(APITestCase):
#     def test_create_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('like-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)



# class CommentsTests(APITestCase):
#     def test_create_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """

#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, tweet=tweet)

#         url = reverse('comments-list')
#         data = {'tweet': tweet.id, "user": user.id,'text':'babaaaaa eba lo le shey  babaaaaa'}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_comments(self):
#         """
#         Ensure we can get a new commnt object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, tweet=tweet)

#         url = reverse('comments-list')
#         response = self.client.get(url, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Comments.objects.count(), 1)
#         self.assertEqual(response_data[0]['text'], comment.text)
          
#     def test_put_comments(self):
#         """
#         Ensure we can put a comment object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, tweet=tweet)

#         url = reverse('comments-detail', kwargs={'pk': comment.id})
#         data = {'tweet': tweet.id, "user": user.id,'text':'oloyede ni awon angeli'}
#         response = self.client.put(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Comments.objects.count(), 1)
           
#     def test_delete_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comment", user=user, tweet=tweet)

#         url = reverse('comments-detail', kwargs={'pk': comment.id})
#         response = self.client.delete(url)

#         print(response.content)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Comments.objects.count(), 0)
     
#     def test_patch_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comment", user=user, tweet=tweet)

#         url = reverse('comments-detail', kwargs={'pk':comment.id})
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.patch(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Comments.objects.count(), 1)
        