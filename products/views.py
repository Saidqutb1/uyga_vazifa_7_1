from django.shortcuts import render
from rest_framework.response import Response

from .serializers import CategoryGoodsSerializers, GoodsSerializers
from .models import Category, Goods
from rest_framework.views import APIView
# Create your views here.


class ListCategoryAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategoryGoodsSerializers(category, many=True)
        serializer_data = {
            'category': serializer.data,
            'status': 'success'
        }
        return Response(serializer_data)
