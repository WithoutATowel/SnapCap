from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    path('snaps/', views.snaps, name='snaps'),
    path('snaps/<int:snap_id>/', views.details, name='details'),
    path('snaps/friends/', views.friends, name='friends'),
    path('snaps/<str:category>/', views.category, name='category'),
    path('snaps/<int:snap_id>/vote/', views.snap_vote, name='snap_vote'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('caps/<int:cap_id>/<int:is_card>/', views.cap_vote, name='cap_vote'),
]
