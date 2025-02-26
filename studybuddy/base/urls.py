from django.urls import path
from . import views
from .views import redirect_to_instagram




urlpatterns = [
     path('',views.home, name='home'),
     
     path('room/<str:pk>', views.room, name='room'), 
    
     path('create-room/', views.createRoom, name='create-room'),
    
     path('update-room/<str:pk>', views.updateRoom, name='update-room'),
     path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
     
     path('login/', views.loginView, name='login'),
     path('logout/', views.logoutView, name='logout'),
     path('register/', views.registerPage, name='register'),

     path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
     path('update-user/', views.updateUser, name='update-user'),

     path('profile/<str:pk>', views.userProfile, name='user-profile'),

     path('topic/', views.topicPage, name='topic'),
     path('activity/', views.activityPage, name='activity'),


     path('go-to-insta/', views.redirect_to_instagram, name='redirect_to_instagram'),


]



