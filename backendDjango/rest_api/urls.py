from django.urls import path, include
from .views import PostsView, detail, PostViewSet, PostsAPIView, postDetailsAPIView, genericAPIView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('postsl/', PostsView),
    # path('detail/<int:pk>',detail)

    # path('postsapiview/', PostsAPIView.as_view()),
    # path('detailapiview/<int:pk>',postDetailsAPIView.as_view())
    path('genericapiview/<int:id>/', genericAPIView.as_view()),
    path('',include(router.urls)),

]