from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('index.html', views.index),
    path('about', views.about),
    path('blog', views.blog),
    path('contact', views.contact,name='contact'),
    path('doctors', views.doctors),
    path('services', views.services),
    path('response',views.response, name='response'),
    #path('login', views.login,name='login'),
]
