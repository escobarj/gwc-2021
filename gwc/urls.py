from django.urls import path
from . import views

# GWC-Comment: We tell Django about new pages by adding the to urlpatterns.
#    Example: path('blog', views.blog, name='blog'),
#    The first parameter to path() is the name of the page in the page url, ex: http://www.mysite.com/BLOG/
#    The second parameter is the corresponding function name in views.py, ex: views.BLOG
#    The last parameter is a name for the page that you can use in html, ex: {% url BLOG %}
urlpatterns = [
    path('', views.homepage, name='home'),
    path('joke/', views.joke, name='joke'),
    path('count/', views.count, name='count'),
    path('result/', views.result, name='result'),
    path('events/', views.events, name='events'),
    path('puzzles/', views.puzzles, name='puzzles'),
    path('resources/', views.resources, name='resources'),
]
