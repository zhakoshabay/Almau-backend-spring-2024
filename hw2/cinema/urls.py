from django.urls import path
from .views import index_page, movie_details

urlpatterns = [
    path('', index_page),
    path('<int:pk>', movie_details)
]