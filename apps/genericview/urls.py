from django.urls import path, include
from . import views

urlpatterns = [
    path('authors/', views.AuthorListAPIView.as_view(), name='author_list'),
    path('author/create', views.AuthorCreateAPIView.as_view(), name='author_create'),
    path('author/retrive/<int:pk>/', views.AuthorRetrieveAPIView.as_view(), name='author_retrieve'),
    path('author/update/<int:pk>/', views.AuthorUpdateAPIView.as_view(), name='author_update'),
    path('author/destroy/<int:pk>/', views.AuthorDestroyAPIView.as_view(), name='author_destroy'),


    path('authors/list/create/', views.AuthorListCreateView.as_view()),
    path('author/rud/<int:pk>', views.AuthorRetrieveUpdateDestroyView.as_view())
]
