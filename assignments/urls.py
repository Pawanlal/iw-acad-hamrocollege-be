from rest_framework.routers import DefaultRouter

from .views import AssignmentModelViewSet, SubmissionModelViewSet

r = DefaultRouter()
r.register('assignment', AssignmentModelViewSet)
r.register('submission', SubmissionModelViewSet)


app_name = 'assignments'

urlpatterns = [

] + r.urls