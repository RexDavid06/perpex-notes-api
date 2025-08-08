from django.urls import path, include
from .views import NoteViewSet, RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'noteapp'
router = DefaultRouter()
router.register('notes', NoteViewSet, basename='note')

urlpatterns = [ 
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token, name='api-token-auth'),#this endpoint allow users obtain an authentication token
    path("register/", RegisterView.as_view(), name='register'),
]