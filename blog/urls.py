from django.urls import path
from . import views
from .views import View, CreatePostView

urlpatterns = [
    path('', View.as_view(), name='post_list'),
    path('post/<int:pk>/edit/', CreatePostView.as_view(), name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
