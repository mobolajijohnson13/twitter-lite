from post.views import index
from django.urls import path,include

urlpatterns = [
    path('index/', index),
    
]