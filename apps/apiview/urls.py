from django.urls import path
from .views import AuthorAPIView, AuthorRUDView

urlpatterns = [
    path('authors/list-create/', AuthorAPIView.as_view()),
    path('author/rud/<int:pk>/', AuthorRUDView.as_view())
]