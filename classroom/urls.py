from django.urls import path
from .views import CreateClassroom, AddMembers,DiscussionForum

app_name = 'classroom'

urlpatterns = [
    path('create/', CreateClassroom.as_view(),name='create'),
    path('members/', AddMembers.as_view(), name='member'),
    path('forum/', DiscussionForum.as_view(), name='forum'),
]