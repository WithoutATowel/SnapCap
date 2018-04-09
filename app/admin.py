from django.contrib import admin
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship

admin.site.register(Profile)
admin.site.register(Picture)
admin.site.register(Usercap)
admin.site.register(Vote_Picture)
admin.site.register(Vote_Caption)
admin.site.register(Friendship)