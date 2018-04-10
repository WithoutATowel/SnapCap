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
from .serializers import ProfileSerializer, PictureSerializer, UsercapSerializer, Vote_PictureSerializer, Vote_CaptionSerializer, FriendshipSerializer, UserSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PictureView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    # Get a snap's caps:
    # Picture.objects.get(id=1).usercap_set.all()

    # Get all the snaps that have a cap with a given word or phrase
    # matching_caps = Usercap.objects.filter(text__icontains = 'oh')
    # Picture.objects.filter(id__in = [cap.picture.id for cap in matching_caps])

    def get_queryset(self):
        # __icontains() for cap text?
        queryset = Picture.objects.all()
        username = self.request.query_params.get('username', None)
        if 'category' in self.kwargs.keys():
            queryset = queryset.filter(category = self.kwargs['category'])
        elif username is not None:
            queryset = queryset.filter(user__username='username')
        return queryset

class UsercapView(viewsets.ModelViewSet):
    queryset = Usercap.objects.all()
    serializer_class = UsercapSerializer

class Vote_PictureView(viewsets.ModelViewSet):
    queryset = Vote_Picture.objects.all()
    serializer_class = Vote_PictureSerializer

class Vote_CaptionView(viewsets.ModelViewSet):
    queryset = Vote_Caption.objects.all()
    serializer_class = Vote_CaptionSerializer

class FriendshipView(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

def index(request):
    print('okay')
    return render(request, 'index.html')

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny] # Or anon users can't register
    serializer_class = UserSerializer














# def signup(request):
    # FROM CAT COLLECTOR:
    # from django.contrib.auth import authenticate, login, logout
    #
    # FROM CAT COLLECTOR:
    # if request.method == 'POST':
    #     print('hit the route')
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         print('form is valid')
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('/')
    # else:
    #     form = SignUpForm()
    # return render(request, 'signup.html', {'form': form})
#   return HttpResponse("User registered.")

# def login(request):
    # FROM CAT COLLECTOR:
    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         u = form.cleaned_data['username']
    #         p = form.cleaned_data['password']
    #         user = authenticate(username = u, password = p)
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect('/')
    #             else:
    #                 print("This account has been disabled")
    #         else:
    #             form = LoginForm()
    #             return render(request, 'login.html', {'form':form})
    #     else: 
    #         form = LoginForm()
    #         return render(request, 'login.html', {'form':form})
    # else: 
    #     form = LoginForm()
    #     return render(request, 'login.html', {'form':form})
    # return HttpResponse("Login successful.")

# def logout(request):
    # FROM CAT COLLECTOR:
    # logout(request)
    # return HttpResponseRedirect('/')
    # return HttpResponse("Logout successful.")

# def snaps(request):
#     # if HttpRequest.GET:
#     #     data = 
#     # else:
#     data = serializers.serialize("json", Picture.objects.all())
#     return HttpResponse(data, content_type='application/json')

# def details(request, snap_id):
#     # Picture.objects.get(pk=toy_id)
#     data = serializers.serialize("json", Picture.objects.get(pk=snap_id))
#     return HttpResponse(data, content_type='application/json')

# def friends(request):
#     # Picture.objects.filter()
#     data = { "test": "friends route"}
#     return HttpResponse(data, content_type='application/json')

# def category(request, category):
#     # Picture.objects.filter()
#     data = { "test": "category route"}
#     return HttpResponse(data, content_type='application/json')

# def snap_vote(request, snap_id):
#     return HttpResponse("Snap vote recorded.")


# def profile(request, profile_id):
#     if request.method == "GET":
#         data = { "test": "profile route"}
#         return HttpResponse(data, content_type='application/json')
#     if request.method == "PUT":
#         return HttpResponse("Profile updated.")
#     if request.method == "DELETE":
#         return HttpResponse("Profile deleted.")

# def cap_vote(request, cap_id, is_card):
#     return HttpResponse("Snap vote recorded.")
