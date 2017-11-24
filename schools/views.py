from django.shortcuts import render, redirect, get_object_or_404
from .models import School
from django.template.defaultfilters import slugify




# Create your views here.
def all_schools(request):
    schools = School.objects.all()
    return render(request, "schools.html",{"schools": schools})

def view_school(request, slug):
    school = get_object_or_404(School, slug=slug)
    return render(request, "school.html",{"school": school}) 
    
# def viewpost(request, id):
#     post = get_object_or_404(Post, pk=id)
#     comments = Comment.objects.filter(post= post)
#     form = BlogCommentForm()
#     return render(request, "viewpost.html", {'post': post, 'comments': comments, 'form': form}) 
    
