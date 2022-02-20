from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import message
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from .models import *




def all(request):
   new1=Flight.objects.all()
   print(new1)
   return  render(request,"show.html",{"new1":new1})

def update(request,id):
   context = {}


   obj = get_object_or_404(Flight, id=id)


   form = FlightForm(request.POST or None, instance=obj)


   if form.is_valid():
      form.save()
      return HttpResponseRedirect("/all")


   context["form"] = form

   return render(request, "update.html", context)


def delete(request,id):
   obj = get_object_or_404(Flight, id=id)
   obj.delete()
   return HttpResponseRedirect("/all")











