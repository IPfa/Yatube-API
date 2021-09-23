from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowList, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/groups', GroupViewSet)
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowList.as_view()),
]
