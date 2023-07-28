from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    isbn = serializers.CharField(max_length=13)
    genre = serializers.CharField(max_length=8)


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
