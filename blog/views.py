from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.template.defaultfilters import slugify

# Create your views here.
def blogposts(request):
    blogposts = BlogPost.objects.all()
    return render(request, "blogposts.html", {'blogposts':blogposts})
    
def viewpost(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    return render(request, "viewpost.html", {'blogpost': blogpost}) 
    


    

   