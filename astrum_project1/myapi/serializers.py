from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'age']  #if you want to change fields
