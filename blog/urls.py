from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:blog_id>/', views.detail, name = 'detail'),  
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'), # views의 create 함수 호출
    path('newblog/', views.blogpost, name = "newblog"),
    path('edit/<int:blog_id>', views.blogpost, name = "edit"),
    path('delete/<int:blog_id>', views.delete, name = "delete"),
]