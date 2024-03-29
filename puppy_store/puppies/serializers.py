from rest_framework import serializers
from .models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'created_at', 'updated_at')
        