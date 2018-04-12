from django.conf.urls import url
from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('profile', views.ProfileView)
router.register('snaps', views.PictureView)
router.register('caps', views.UsercapView)
router.register('vote_picture', views.Vote_PictureView)
router.register('vote_caption', views.Vote_CaptionView)
router.register('friends', views.FriendshipView)

urlpatterns = [
    path('', views.index, name='index'),
    url('api/snaps/(?P<category>\D+)/$', views.PictureView.as_view({'get': 'list'})),
    re_path('api/snaps/(?P<category>\D+)/(?P<user_id>[0-9]+)/$', views.PictureView.as_view({'get': 'list'})),
    url('auth/obtain_token/', obtain_jwt_token),
    url('auth/refresh_token/', refresh_jwt_token),
    path('api/user/<int:user_id>/friends/', views.FriendsListView, name='friends_list'),
    path('api/user/<int:user_id>/caps/', views.CapsListView, name='caps_list'),
    path('api/friends/<int:user_id>/<int:friend_id>/', views.follow, name='follow'),
    path('api/', include(router.urls)),
]
