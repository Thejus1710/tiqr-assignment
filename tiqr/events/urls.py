from django.urls import path

from .views import UserList, CreateUser, EventList

from . import views

urlpatterns = [
    path("users-list/", UserList.as_view(), name="user-list"),
    path("create-user/", CreateUser.as_view(), name="user-list"),
    path("events-list/", EventList.as_view(), name="event-list")
]