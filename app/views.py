from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import requests
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from .serializers import ProfileSerializer, PictureSerializer, UsercapSerializer, Vote_PictureSerializer, Vote_CaptionSerializer, UserSerializer, FriendshipSerializer
from django.db.models import Count
from datetime import date, timedelta

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # Need to set permissions so that a user can only edit their own

class PictureView(viewsets.ModelViewSet):
    queryset = Picture.objects.filter(uploaded_date__gt=date.today()-timedelta(days=7))
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Get all the snaps that have a cap with a given word or phrase
    # matching_caps = Usercap.objects.filter(text__icontains = 'oh')
    # Picture.objects.filter(id__in = [cap.picture.id for cap in matching_caps])

    def get_queryset(self):
        # __icontains() for cap text + search?
        queryset = Picture.objects.all().filter(uploaded_date__gt=date.today()-timedelta(days=7))
        username = self.request.query_params.get('username', None)
        if 'category' in self.kwargs.keys():
            if self.kwargs['category'] == 'friends':
                friends = Friendship.objects.filter(user_id = 5)
                queryset = queryset.filter(user__id__in = [friend.friend_id for friend in friends])
            else:
                queryset = queryset.filter(category = self.kwargs['category'])
        elif username is not None:
            queryset = queryset.filter(user__username = 'username')
        queryset = queryset.annotate(votes=Count('vote_picture')).order_by('-votes')
        return queryset


class UsercapView(viewsets.ModelViewSet):
    queryset = Usercap.objects.all()
    serializer_class = UsercapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Vote_PictureView(viewsets.ModelViewSet):
    queryset = Vote_Picture.objects.all()
    serializer_class = Vote_PictureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Vote_CaptionView(viewsets.ModelViewSet):
    queryset = Vote_Caption.objects.all()
    serializer_class = Vote_CaptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def index(request):
    print('okay')
    return render(request, 'index.html')

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny] # Or anon users can't register
    serializer_class = UserSerializer
    # Need to set permissions so that anyone can *sign up* but a user can only edit their own profile

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }

def FriendsListView(request, user_id):
    friend_ids = Friendship.objects.filter(user=user_id)
    friends = User.objects.filter(id__in = [friend.friend.id for friend in friend_ids])
    # friends = User.objects.filter(id__in = [friend.friend.id for friend in friend_ids]).values('first_name', 'last_name').annotate(profile_img_url=)
    friends = serializers.serialize('json', list(friends), fields=('id', 'first_name', 'last_name'))
    return HttpResponse(friends, content_type='application/json')
