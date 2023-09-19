from rest_framework import serializers
from .models import LibraryBook

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=LibraryBook
		fields='__all__'

