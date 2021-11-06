from datetime import datetime
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from women.forms import *

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

def index(request):
    posts = Women.objects.all()

    insert_content = {
        'posts': posts,
        'menu': menu, 
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=insert_content)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')            
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    insert_content = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=insert_content)
    
# def show_category(request, cat_slug):
#     cats = Category.objects.all()
#     cat = get_object_or_404(Category, slug =cat_slug)
#     posts = Women.objects.filter(cat_id=cat.id)

#     if len(posts) == 0:
#         raise Http404()

#     insert_content = {
#         'posts': posts,
#         'menu': menu,
#         'cats': cats,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_slug,
#     }

#     return render(request, 'women/index.html', context=insert_content)

def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug) # берем посты определенной категории
                                                     # cat__slug это обращение к модели Category через Women
                                                     # в Women через поле cat хранятся все соответствующие данные модели Category
    if len(posts) == 0:
        raise Http404()

    insert_content = {
        'posts': posts,
        'menu': menu,
        'cat_selected': cat_slug,
    }

    return render(request, 'women/index.html', context=insert_content)