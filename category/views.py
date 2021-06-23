from django.shortcuts import render
from rest_framework import generics, permissions

from category import serializers
from category.models import Category


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAdminUser,)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieve update, delete books review
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAdminUser,)

