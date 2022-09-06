from django.shortcuts import render, redirect
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


# 추가 뷰
def search(request):
    movies = Movie.objects.filter(title__contains=request.GET.get('title'))
    context = {
        'movies': movies,
    }
    return render(request, 'movies/search.html', context)


def new(request):
    return render(request, 'movies/new.html')


def create(request):
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.trailer_url = request.POST.get('trailer_url')
    movie.review = request.POST.get('review')
    movie.save()
    return redirect('movies:detail', movie.pk)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.trailer_url = request.POST.get('trailer_url')
    movie.review = request.POST.get('review')
    movie.save()
    return redirect('movies:detail', movie.pk)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
