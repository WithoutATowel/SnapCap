from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# How to customize your join table with extra fields, which we'll need for Cards_Users:
# https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships

# User model base fields:
# https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User
# How to extend the User model:
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model

# Extends the user model via a 1:1 mapping
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.CharField(max_length=1000)

CATEGORY = (
    ('animals', 'animals'),
    ('cats', 'cats'),
    ('dogs', 'dogs'),
    ('sports', 'sports'),
    ('hummus', 'hummus'),
)

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cloudinary_url = models.CharField(max_length=1000)
    category = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self):
        return self.cloudinary_url

class Usercap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, related_name='usercaps', on_delete=models.CASCADE)
    text = models.CharField(max_length=140)

    def __unicode__(self):
        return self.text
    
    def __str__(self):
        return self.text

class Vote_Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

class Vote_Caption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    usercap = models.ForeignKey(Usercap, on_delete=models.CASCADE)

STATUS = (
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected'),
)

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_of')
    status = models.IntegerField(choices=STATUS)

# class Card(models.Model):
#     text = models.CharField(max_length=140)
