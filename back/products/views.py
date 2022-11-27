from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product, Category
from django.shortcuts import render, Http404


class ProductsList(APIView):
    def get(self, request, format=None):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return

    def get(self, request, category_slug, product_slug, format=None):
        products = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(products)
        print(serializer.data)
        return Response(serializer.data)
