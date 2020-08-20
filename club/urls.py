
from rest_framework.routers import DefaultRouter

from .views import AnnouncementModelViewSet, ClubModelViewSet, MemberModelViewSet

r = DefaultRouter()
r.register('announcement', AnnouncementModelViewSet)
r.register('club', ClubModelViewSet)
r.register('member', MemberModelViewSet)


app_name = 'club'

urlpatterns = [

]+ r.urls