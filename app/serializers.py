from rest_framework import serializers
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_img')


class UsercapSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Usercap
        fields = ('id', 'user', 'picture', 'text', 'votes')

    def get_votes(self, obj):
        return obj.vote_caption_set.count()


class PictureSerializer(serializers.ModelSerializer):
    usercaps = UsercapSerializer(many=True, read_only=True)
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ('id', 'user', 'cloudinary_url', 'category', 'usercaps', 'votes')

    def get_votes(self, obj):
        return obj.vote_picture_set.count()


class Vote_PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_Picture
        fields = ('id', 'user', 'picture')
        validators = [
            UniqueTogetherValidator(
                queryset=Vote_Picture.objects.all(),
                fields=('user', 'picture')
            )
        ]


class Vote_CaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_Caption
        fields = ('id', 'user', 'picture')
        validators = [
            UniqueTogetherValidator(
                queryset=Vote_Caption.objects.all(),
                fields=('user', 'picture')
            )
        ]


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'user', 'friend', 'status')


class UserSerializer(serializers.ModelSerializer):
    # Fields: https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        max_length=150,
        validators= [UniqueValidator(
            queryset=User.objects.all(),
            message='That username already exists, bro',
        )]
    )
    friends = FriendshipSerializer(many=True, read_only=True)
    picture_set = PictureSerializer(many=True, read_only=True, allow_null=True)
    usercap_set = UsercapSerializer(many=True, read_only=True, allow_null=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'friends', 'picture_set', 'usercap_set')
        write_only_fields = ('password', )
        read_only_fields = ('id', )
