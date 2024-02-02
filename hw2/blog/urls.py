from django.urls import path
from .views import index_page, article_details

urlpatterns = [
    path('', index_page),
    path('<int:pk>', article_details)
]