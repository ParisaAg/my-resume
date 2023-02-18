from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from resume.models import Post
from resume.models import contact
from .forms import *
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def test(request):
    posts= Post.objects.all()
    context = {'posts':posts}
    return render(request,'index.html',context)


def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('its done thanks!')
        else:
            return HttpResponse('not valid!!')
    
    form = ContactForm()
    return render(request,'form.html',{'form':form})


def contact_view(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks! we already have your messages')
        else:
            messages.add_message(request,messages.error,'sorry, please try again!')
            return HttpResponseRedirect('/contact')
    form = ContactForm()
    return render(request,'index.html',{'form':form})
    

# Create your views here.
