from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from . form import Movie_update
# Create your views here.
def index(request):
    movie=Movie.objects.all()

    context={
        'movielist':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mini_desc = request.POST.get('mini_desc')
        desc=request.POST.get('desc')
        Year = request.POST.get('Year')
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,mini_desc=mini_desc, Year=Year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movie_update(request.POST or None,request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')