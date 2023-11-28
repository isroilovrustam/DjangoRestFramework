from rest_framework import serializers
from .models import AuthorAPI, CategoryAPI, BookAPI


class AuthorAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorAPI
        fields = ['id', 'first_name', 'last_name', 'age', 'job']