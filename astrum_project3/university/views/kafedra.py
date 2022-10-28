from rest_framework.views import APIView
from Django_REST.astrum_project3.university.models import Kafedra
from Django_REST.astrum_project3.university.serializer import KafedraSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class KafedraListCreateView(APIView):

    def get(self, request):
        queryset = Kafedra.objects.all()
        serializer = KafedraSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KafedraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class KafedraDetailView(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Kafedra, pk=pk)
        serializer = KafedraSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = get_object_or_404(Kafedra, pk=pk)
        serializer = KafedraSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = get_object_or_404(Kafedra, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
