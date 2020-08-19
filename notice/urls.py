from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryModelViewSet, NoticeModelViewSet, CommentModelViewSet

r = DefaultRouter()
r.register('category', CategoryModelViewSet)
r.register('notice', NoticeModelViewSet)
r.register('comment', CommentModelViewSet)

app_name = 'notice'
urlpatterns = [
] + r.urls
