from rest_framework import serializers
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_img')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'user', 'cloudinary_url', 'category')

class UsercapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercap
        fields = ('id', 'user', 'picture', 'text', 'votes')

class Vote_PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_Picture
        fields = ('id', 'user', 'picture')

class Vote_CaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_Caption
        fields = ('id', 'user', 'picture')

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'user', 'friend', 'status')

