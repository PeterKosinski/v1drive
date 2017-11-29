from django.shortcuts import render, redirect, get_object_or_404
from .models import School
from django.template.defaultfilters import slugify




# Create your views here.
def all_schools(request):
    schools = School.objects.all()
    return render(request, "schools.html",{"schools": schools})

def view_school(request, slug):
    school = get_object_or_404(School, slug=slug)
    related = School.objects.all().order_by('Lesson_Price_For_12')[:3]
    return render(request, "school.html",{"school": school, "related" : related}) 
    
def do_search(request):
    schools = School.objects.filter(Area__icontains=request.GET['q'])
    return render(request, "schools.html", {"schools": schools})        
    
