from rest_framework.views import APIView
from .models import AuthorAPI
from .serializers import AuthorAPISerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class AuthorAPIView(APIView):
    def get(self, request):
        queryset = AuthorAPI.objects.all()
        serializer = AuthorAPISerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorRUDView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(AuthorAPI, pk=pk)
        serializer = AuthorAPISerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(AuthorAPI, pk=pk)
        serializer = AuthorAPISerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = get_object_or_404(AuthorAPI, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
