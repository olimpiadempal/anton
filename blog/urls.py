from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('category/Essen/', views.post_category_essen, name='post_category_essen'),
    path('category/Koerper/', views.post_category_koerper, name='post_category_koerper'),
    path('category/Sport/', views.post_category_sport, name='post_category_sport'),
    path('category/Lifestyle/', views.post_category_lifestyle, name='post_category_lifestyle'),
    path('category/Anders/', views.post_category_anders, name='post_category_anders'),
]