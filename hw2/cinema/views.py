from django.shortcuts import render
from .models import Movie

# Create your views here.

def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', { 'movies': movies })

def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'article_details.html', { 'movie': movie })
