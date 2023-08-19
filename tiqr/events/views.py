from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Event, User
from rest_framework.response import Response
from .serilaizers import UserSerializer
# Create your views here.


class EventList(APIView):

    def get(self, request, *args, **kwargs):
        events = Event.objects.all().values("id","creator", "creator__first_name")
        return Response(data=events)


class UserList(APIView):

    def get(self, request, *args, **kwargs):
        events = User.objects.all().values()
        return Response(data=events)


class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.create(**data)
            return Response(data=user.fullname)
        except:
            return Response(data="Failed to create user")




