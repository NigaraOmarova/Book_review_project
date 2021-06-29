
from rest_framework import generics, permissions

from book.permissions import IsAccountOwnerOrReadOnly
from rating import serializers
from .models import Mark


class MarkCreateView(generics.CreateAPIView):
    serializer_class = serializers.MarkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MarkDeleteView(generics.DestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAccountOwnerOrReadOnly)

