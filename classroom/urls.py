
from rest_framework.routers import DefaultRouter

from .views import ClassroomModelViewSet, ClassroomDiscussionModelViewSet, ClassroomMemberModelViewSet, CommentModelViewSet

r = DefaultRouter()
r.register('classroom', ClassroomModelViewSet)
r.register('discussion', ClassroomDiscussionModelViewSet)
r.register('member', ClassroomMemberModelViewSet)
r.register('comment', CommentModelViewSet)


app_name = 'classroom'

urlpatterns = [

] + r.urls
