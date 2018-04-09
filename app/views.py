from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def snaps(request):
    # if HttpRequest.GET:
    #     data = 
    # else:
    data = serializers.serialize("json", Picture.objects.all())
    return HttpResponse(data, content_type='application/json')

def details(request, snap_id):
    # Picture.objects.get(pk=toy_id)
    data = serializers.serialize("json", Picture.objects.get(pk=snap_id))
    return HttpResponse(data, content_type='application/json')

def friends(request):
    # Picture.objects.filter()
    data = { "test": "friends route"}
    return HttpResponse(data, content_type='application/json')

def category(request, category):
    # Picture.objects.filter()
    data = { "test": "category route"}
    return HttpResponse(data, content_type='application/json')

def snap_vote(request, snap_id):
    return HttpResponse("Snap vote recorded.")

def signup(request):
    return HttpResponse("User registered.")

def login(request):
    return HttpResponse("Login successful.")

def logout(request):
    return HttpResponse("Logout successful.")

def profile(request, profile_id):
    if request.method == "GET":
        data = { "test": "profile route"}
        return HttpResponse(data, content_type='application/json')
    if request.method == "PUT":
        return HttpResponse("Profile updated.")
    if request.method == "DELETE":
        return HttpResponse("Profile deleted.")

def cap_vote(request, cap_id, is_card):
    return HttpResponse("Snap vote recorded.")
