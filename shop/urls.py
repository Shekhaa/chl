from django.contrib import admin
from django.urls import path
from shop import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name="about"),
    path('ok',views.ok,name='ok'),
    path('product',views.product,name='product'),
    path('calc',views.calc,name='calc'),
    path('search',views.search,name='search'),
    path('page',views.page,name='page'),
    path('<str:slu>',views.blogposts,name="blogposts"),
]




