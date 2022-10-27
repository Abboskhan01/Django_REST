from rest_framework import routers, generics
# from .views import AuthorViewSet
from .models import Author
from .serializers import AuthorSerializer
from django.urls import path, include
from .views import *

# router = routers.DefaultRouter()
# router.register(r'authors', AuthorViewSet)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='Authors_list'),
    path('authors/<pk>/', AuthorRetrieveView.as_view(), name='Author'),
    # path('authors/<pk>', AuthorDestroyView.as_view(), name='Author'),
    # path('authors/<pk>', AuthorCreateView.as_view(), name='Author'),
    # path('authors/<pk>', AuthorUpdateView.as_view(), name='Author'),
    path('user/', generics.ListCreateAPIView.as_view(queryset=Author.objects.all(), serializer_class=AuthorSerializer))
]