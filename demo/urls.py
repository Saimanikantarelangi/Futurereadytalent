from django.contrib.auth.views import LoginView

from . import views
from .views import *
from django.urls import path



urlpatterns=[


    path('all',all,name="show"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete")

]