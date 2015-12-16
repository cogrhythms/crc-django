from crc.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'index.html',{})

def faculty(request):
    people_list = People.objects.get(position='F')
    return render(request,'faculty_page.html', {'faculty' : people_list})

def postdocs(request):
    people_list = People.objects.get(position='PD')
    return render(request, 'postdoc_page.html', {'postdocs' : people_list})

def topics(request):
    topic_list = Topics.objects.all()
    return render(request, 'topics_page.html', {'topics' : topic_list})

def groups(request):
    group_list = Groups.objects.all()
    return render(request, 'groups_page.html', {'groups': group_list})

def courses(request):
    course_list = Courses.objects.all()
    return render(request, 'courses_page.html', {'courses': course_list})
