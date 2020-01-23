from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles':articles})

def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', {'article':article})

def search_result(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__contains=query)
    return render(request, 'search.html', {'articles':articles})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')
    else:
        form = forms.CreateArticle()
    return render(request, 'article_create.html', {'form':form})