from rest_framework import serializers
from .models import Product

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ['id','title','price','image']