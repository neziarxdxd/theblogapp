from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BlogPost
def index(request):
    return HttpResponse("Hello, World!")
def myName(request):

    return HttpResponse("testing xxD")
def show_blog_post(request):
    obj = BlogPost.objects.get(id=1)
    context= {
        'blog':obj
    }
    
    return render(request,"blogpost.html",context)
