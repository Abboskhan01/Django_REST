from rest_framework import routers
from .views import AuthorViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
