from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, BookViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"author", AuthorViewSet)
router.register(r"book", BookViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
