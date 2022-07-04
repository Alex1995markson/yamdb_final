from api.views import (APISignup, CategoryViewSet, CodeConfirmView,
                       CommentViewSet, GenreViewSet, ReviewViewSet,
                       TitleViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.register(
    prefix=r'categories',
    viewset=CategoryViewSet,
    basename='categories',
)
v1_router.register(
    prefix=r'genres',
    viewset=GenreViewSet,
    basename='genres',
)
v1_router.register(
    prefix=r'titles',
    viewset=TitleViewSet,
    basename='titles',
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(r'users', UserViewSet)

auth_patterns = [
    path(
        'token/',
        CodeConfirmView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'signup/',
        APISignup.as_view(),
        name='signup'
    )
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('', include(v1_router.urls)),
    path('v1/auth/', include(auth_patterns))
]
