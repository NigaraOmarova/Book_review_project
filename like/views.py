
from rest_framework import generics, permissions

from book.permissions import IsAccountOwnerOrReadOnly
from like import serializers
from .models import Like



class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAccountOwnerOrReadOnly)

