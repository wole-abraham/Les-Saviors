from django.shortcuts import render
from .models import Course

# Create your views here.


def courses(request, id=0):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        url = request.POST.get('url')
        # if 'youtu.be' in url:
        #     url = 
        Course.objects.create(title=title, description=description,
                              url=url)
        
    elif request.method == "DELETE":
        course = Course.objects.filter(id=id)
        course.delete()



    return render(request, 'courses/courses.html', {"courses": Course.objects.all()})