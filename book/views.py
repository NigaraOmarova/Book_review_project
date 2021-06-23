from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from book import serializers
from book.models import BookReview, Comment

from .permissions import IsReviewOwnerOrReadOnly


class StandardResultsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BookReviewCreateView(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for list and create books review
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = BookReview.objects.all()
    serializer_class = serializers.ReviewSerializer
    pagination_class = StandardResultsPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'owner')
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieve update, delete books review
    """
    queryset = BookReview.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsReviewOwnerOrReadOnly)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsReviewOwnerOrReadOnly)

