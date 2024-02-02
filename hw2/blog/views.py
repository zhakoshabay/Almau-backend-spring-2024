from django.shortcuts import render
from .models import Article

# Create your views here.

def index_page(request):
    articles = Article.objects.all()
    return render(request, 'index.html', { 'articles': articles })

def article_details(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'article_details.html', { 'article': article })
