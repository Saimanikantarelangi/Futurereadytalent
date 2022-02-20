from django.urls import path
from .views import *

urlpatterns = [
    path('', latest, name='latest'),
    path('register',register ,name='register'),
    path('login',login ,name='login'),
    path('home/', home, name='home'),
    path('search', search, name='search'),
    path('addpost',addpost, name='search')



]
