from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryModelViewSet, NoticeModelViewSet

r = DefaultRouter()
r.register('category', CategoryModelViewSet)
r.register('notice', NoticeModelViewSet)

app_name = 'notice'
urlpatterns = [
    # path('notice/', NoticeModelViewSet.as_view())
] + r.urls
