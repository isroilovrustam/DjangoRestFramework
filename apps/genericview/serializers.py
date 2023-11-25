from rest_framework import serializers
from .models import AuthorGeneric, CategoryGeneric, BookGeneric


class AuthorGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorGeneric
        fields = ['id', 'first_name', 'last_name', 'age', 'job']


class CategoryGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGeneric
        fields = ['title', ]


class BookGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGeneric
        fields = ['title', 'author', 'category', 'language', 'numbers_of_books']

