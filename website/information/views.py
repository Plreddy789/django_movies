from django.http import request, HttpResponse
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
