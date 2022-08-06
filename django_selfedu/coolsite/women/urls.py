from django.urls import path, re_path
from .views import *

# связывает функции предстваления из view с соответствующими url
urlpatterns = [
    # всегда давать имена, чтобы избежать hard coding
    path('', WomenHome.as_view(), name='home'), 
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # путь с передачей в него параметра
    path('post/<int:post_id>', ShowPost.as_view(), name='post'),
    path('category/<int:cat_id>', show_category, name='category'),
    # путь прописан с помощью регулярного выражения, принимающий параметр <год>
    re_path(r'^archive/(?P<year>[0-9]{4})', archive),
    path('test/', ContactClass.as_view())
]
