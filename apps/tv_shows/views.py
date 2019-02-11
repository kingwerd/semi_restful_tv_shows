from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime

def shows(request):
    if request.method == "GET":
        shows = Show.objects.all()
        context = {
            'shows': shows
        }
        return render(request, 'tv_shows/shows.html', context)

def new_show(request):
    if request.method == "GET":
        return render(request, 'tv_shows/new_show.html')
    elif request.method == "POST":
        data = request.POST
        title = data['title']
        network = data['network']
        release_date = data['release_date']
        description = data['description']
        show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        show.save()
        return redirect('/')

def show(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)
        date = show.release_date.strftime('%Y-%m-%d')
        context = {
            'show': show,
            'date': date
        }
        return render(request, 'tv_shows/show.html', context)

def edit(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)
        date = show.release_date.strftime('%Y-%m-%d')
        context = {
            'show': show,
            'date': date
        }
        return render(request, 'tv_shows/edit.html', context)
    if request.method == "POST":
        data = request.POST
        show = Show.objects.get(id=id)
        show.title = data['title']
        show.network = data['network']
        show.release_date = data['release_date']
        show.description = data['description']
        show.save()
        return redirect(f'shows/{id}')

def delete(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)
        show.delete()
        return redirect('/shows')