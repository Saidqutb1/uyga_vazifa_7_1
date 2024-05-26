from rest_framework import serializers
from .models import Category, Goods


class CategoryGoodsSerializers(serializers.ModelSerializer):
    model = Category
    fields = '__all__'


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'