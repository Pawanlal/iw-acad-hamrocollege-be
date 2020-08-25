from django.urls import path, include

from .views import RegisterGenericAPIView, LoginGenericAPIView, UserGenericAPIView, LogoutAPIView

urlpatterns = [
    path('auth/register/', RegisterGenericAPIView.as_view()),
    path('auth/login/', LoginGenericAPIView.as_view()),
    path('auth/user/', UserGenericAPIView.as_view()),
    path('auth/logout/', LogoutAPIView.as_view()),
]
