from django.shortcuts import render
from rest_framework import generics
from .models import AuthorGeneric, BookGeneric, CategoryGeneric
from .serializers import AuthorGenericSerializer, BookGenericSerializer, CategoryGenericSerializer


# Create your views here.

class AuthorListAPIView(generics.ListAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


class AuthorUpdateAPIView(generics.UpdateAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


class AuthorDestroyAPIView(generics.DestroyAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


""" Umumiy generic views """


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializer



