from django.conf.urls import url
from django.urls import path, re_path, include
from . import views
from rest_framework import routers

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
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    
    # path('snaps/friends/', views.friends, name='friends'),
    # path('snaps/<int:snap_id>/vote/', views.snap_vote, name='snap_vote'),
    
    # path('profile/<int:profile_id>/', views.profile, name='profile'),
    # path('caps/<int:cap_id>/<int:is_card>/', views.cap_vote, name='cap_vote'),
]


# COVERED BY THE REST FRAMEWORK ROUTER
# path('snaps/', views.snaps, name='snaps'),
# path('snaps/<int:snap_id>/', views.details, name='details'),
# path('snaps/<str:category>/', views.category, name='category'),