from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)


urlpatterns = [
    path('', include(router.urls))
]