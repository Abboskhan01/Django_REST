from rest_framework import routers
from .views import AuthorViewSet, BooksSerializer, CategorySerializer
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'category', CategorySerializer)
router.register(r'books', BooksSerializer)


urlpatterns = [
    path('', include(router.urls))
]
