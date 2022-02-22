from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import UserForm
from .models import Posts,User
import requests

def home(request):
    data = Posts.objects.all().order_by('title')
    return render(request,'home.html',{'data':data,})

def register(request):
   if request.method == "POST":

     form=UserForm(request.POST)
     if form.is_valid():

        form.save()
        return render(request,"login.html")

     else:
        return HttpResponse("invalid")

   else:
      form=UserForm()


   return render(request, 'register.html',{"form":form})
def login(request):
   if request.method == 'POST':
      username=request.POST["uname"]
      pass1=request.POST["upass"]
      ex=User.objects.get(Username=username)

      if username==ex.Username and pass1==ex.pass1:
         request.session['username'] = ex.Username
         data = Posts.objects.all().order_by('title').filter(Username=ex)
         return render(request,"home.html",{'data':data,'username':username})
      else:
         return HttpResponse("invalid")
   else:
    return render(request,"login.html")

def search(request):
    res = request.GET['query']
    respons = Posts.objects.filter(title__icontains=res)
    return render(request,'search.html',{'respons':respons})

def latest(request):
    ldata = Posts.objects.all().order_by('-date')
    return render(request,'welcome.html',{'ldata':ldata})
def addpost(request):
    if request.method == "POST":
        title = request.POST["utitle"]
        content = request.POST["ucontent"]
        username = request.session['username']
        ex = User.objects.get(Username=username)
        request.session['username'] = ex.Username

        p = Posts(title=title, content=content,Username=ex)
        p.save()
        data=Posts.objects.filter(Username=ex)
        context={
            "data":data,
        }

        return render(request,"home.html",context)
        #
    else:
        return render(request,"addpost.html")
def postdetail(request,id):

    pdata= Posts.objects.get(id=id)
    return render(request,"post_detail.html",{'pdata':pdata})







# Create your views here.
