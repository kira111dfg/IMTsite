"""
URL configuration for imt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path("imtPage/", views.ImtPage,name='imtPage'),
    path("counter/", views.CounterView,name='counter'),
    path('dishes/', views.ShowDishList.as_view(), name='dishes'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', views.ShowPost.as_view(), name='post'),
    path("dietary/", views.DietaryList.as_view(),name='dietary'),
    path('diet/<slug:slug>/', views.ShowDiet.as_view(), name='diet'),
    path('category1/<slug:slug>/', views.CategoryView1.as_view(), name='category1'),
    path('search/',views.Search.as_view(),name='search'),
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('adddiet/', views.AddDiet.as_view(), name='add_diet'),
    path('posts/<int:user_id>', views.Post.as_view(), name='posts'),
    path('menu/<int:user_id>', views.Menu.as_view(), name='menu'),

]
