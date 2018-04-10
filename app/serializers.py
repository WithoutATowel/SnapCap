from rest_framework import serializers
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_img')

class UsercapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercap
        fields = ('id', 'user', 'picture', 'text', 'votes')

class PictureSerializer(serializers.ModelSerializer):
    usercaps = UsercapSerializer(many=True, read_only=True)
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ('id', 'user', 'cloudinary_url', 'category', 'usercaps', 'vote_count')

    def get_vote_count(self, obj):
        return obj.vote_picture_set.count()

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

