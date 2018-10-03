from django.urls import path
from users.views import UserList , UserDetail , UserSignupAPIView , UserLoginAPIView

app_name = 'users'

urlpatterns = [
    path(r'users/', UserList.as_view()),
    path(r'users/<int:id>/', UserDetail.as_view()),
    path(r'users/register/', UserSignupAPIView.as_view()),
    path(r'users/login/', UserLoginAPIView.as_view()),
]