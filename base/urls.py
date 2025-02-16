# users/urls.py

from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<str:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
]