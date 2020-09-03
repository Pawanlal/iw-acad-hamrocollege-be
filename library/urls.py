from rest_framework.routers import DefaultRouter

from .views import AuthorModelViewSet, PublisherModelViewSet, FineModelViewSet, BookIssueModelViewSet, BookModelViewSet, BookRequestModelViewSet

r = DefaultRouter()
r.register('author', AuthorModelViewSet)
r.register('publisher', PublisherModelViewSet)
r.register('book', BookModelViewSet)
r.register('bookrequest', BookRequestModelViewSet)
r.register('bookissue', BookIssueModelViewSet)
r.register('fine', FineModelViewSet)


app_name = 'library'

urlpatterns = [

] + r.urls