from rest_framework import filters, generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post, User
from .permissions import CustomPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class SubscriptionForbidden(APIException):
    status_code = 400
    default_detail = 'Вы не можете подписаться дважды или на самого себя'
    default_code = 'forbidden'


class BasicViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(BasicViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class CommentViewSet(BasicViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = Post.objects.filter(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post[0])


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        following = serializer.validated_data['following']
        if user == following:
            raise SubscriptionForbidden()
        serializer.save(user=user, following=following)
