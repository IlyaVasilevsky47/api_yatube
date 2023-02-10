from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import PostViewSet, CommentsViewSet, GroupViewSet, FollowViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentsViewSet, basename='comments'
)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
