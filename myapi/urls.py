from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings
urlpatterns = [
    path('', latest, name='latest'),
    path('postdetail/<int:id>',postdetail,name="postdetail"),
    path('register',register ,name='register'),
    path('login',login ,name='login'),
    path('home/', home, name='home'),
    path('search', search, name='search'),
    path('addpost',addpost, name='addpost'),
    path('contact',contact, name='contact'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
