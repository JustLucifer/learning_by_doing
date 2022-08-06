from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView, View
from women.forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'  # можно указать urls.py
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):  # Можно передавать объекты и изменяемые, и неизменяемые
        context = super().get_context_data(**kwargs)  # здесь context ссылается на словарь, в котором уже есть posts
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


'''
функция, которая обрабатывает шаблон с передаными аргументами
request - обязательный аргумент(это ссылка на экземпляр класса HttpRequest).
'''
# def index(request): 
#     posts = Women.objects.all()

#     context = {
#         'menu': menu,
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#         }
    
#     return render(request, 'women/index.html', context=context)

def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
        }
    return render(request, 'women/about.html', context=context)


# class AddPage(CreateView):
#     form_class = AddPostForm
#     template_name = 'women/addpage.html'
#     # success_url: reverse_lazy('home')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)  
#         context['menu'] = menu
#         context['title'] = 'Главная страница'
#         context['cat_selected'] = 0
#         return context

        

def addpage(request):
    if request.method == 'POST':
        print(request.method)
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except Exception:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostForm()
    context={
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form,
        }
    
    return render(request, 'women/addpage.html', context=context)


class ContactClass(View):
    context = {
    'menu': menu,
    'title': 'Обратная связь'
    }
    
    def get(self, request):
        return render(request, 'women/contact.html', context=self.context)
    

def contact(request):
    context = {
    'menu': menu, 
    'title': 'Обратная связь'
    }
    return render(request, 'women/contact.html', context=context)


# простая функция предстваления
def login(request):
    return HttpResponse('Страница входа в личный кабинет')


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    # slug_url_kwarg = 'post_slug'      # Если используем слаг
    pk_url_kwarg = 'post_id'  # Если используем число
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Страница поста'
        return context


# def show_post(request, post_id):
#     post = get_object_or_404(Women, pk=post_id)

#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'women/post.html', context=context)


# class WomenCategory(ListView):
#     model = Women
#     template_name = 'women/index.html'
#     context_object_name = 'posts'
#     allow_empty = False  # Если коллекция posts пустая, генерируется ошибка 404

#     def get_queryset(self):
#         # self.kwargs - словарь с параметрами маршрута, где cat_slug - имя параметра
#         return Women.objects.filter(cat__slug=self.kwargs['cat_slug'])
    

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'menu': menu,
               'title': 'Страница категории',
               'posts': posts,
               'cat_selected': cat_id
               }

    return render(request, 'women/index.html', context=context)


def categories(request, catid):
    # проверка на наличие словаря с параметрами передаными в url
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Список категорий</h1><p>{catid}</p>")


def archive(request, year):
    '''генерация исключения 404 если год выше 2020
    и автоматическое перенаправление на обработчик ошибки 404 '''
    if int(year) == 2020:
        raise Http404()
    '''редирект (по имени) на другую страницу при соответсвию условию,
    код перенаправления с флагом тру = 301, без 302'''
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# обрабатывает исключения 404 
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")