from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('logout/',auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
    path('about', views.about, name='about'),
    path('video/', views.video, name='video'),
    path('uploadVideo/', views.video_feed_sq, name='uploadVideo'),
    path('profile', views.profile, name='profile'),
    path('video_feed/', views.video_feed, name='video_feed')
]
