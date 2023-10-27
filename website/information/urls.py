from django.urls import path

from information.views import movie_list

urlpatterns=[
    path("movies/",movie_list)
]