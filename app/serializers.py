from rest_framework import serializers
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.db.models import Count

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_img')


class UsercapSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()
    submitter = serializers.SerializerMethodField()

    class Meta:
        model = Usercap
        fields = ('id', 'user', 'submitter', 'picture', 'text', 'votes')

    def get_votes(self, obj):
        return obj.vote_caption_set.count()

    def get_submitter(self, obj):
        return obj.user.username

class PictureSerializer(serializers.ModelSerializer):
    usercaps = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()
    submitter = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ('id', 'user', 'submitter', 'cloudinary_url', 'category', 'usercaps', 'votes')

    def get_votes(self, obj):
        return obj.vote_picture_set.count()

    def get_usercaps(self, obj):
        captions = obj.usercaps.all().annotate(votes=Count('vote_caption')).order_by('-votes')
        return UsercapSerializer(captions, many=True).data # read_only=True, allow_null=True

    def get_submitter(self, obj):
        return obj.user.username


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
        fields = ('id', 'user', 'picture', 'usercap')
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
    friends = FriendshipSerializer(many=True, read_only=True, allow_null=True)
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
