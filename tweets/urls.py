from tweets.models import Like
from tweets.views import LikeViewSet, tone
from django.urls import path,include
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from tweets.views import TweetViewSet, tone
from tweets.views import RetweetViewSet

router = routers.DefaultRouter()
router.register(r'', TweetViewSet)
router.register(r'', LikeViewSet)
router.register(r'', RetweetViewSet)
urlpatterns = [
    
    path("tone/", tone),
    path("", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



 