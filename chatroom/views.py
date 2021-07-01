from rest_framework import generics, permissions

from book.permissions import IsReviewOwnerOrReadOnly
from chatroom import serializers
from chatroom.models import Messages, Chatroom


class MessagesCreateView(generics.CreateAPIView):
    serializer_class = serializers.MessagesSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChatroomListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for list and create chat rooms
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Chatroom.objects.all()
    serializer_class = serializers.ChatroomSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChatroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieve update, delete chatroom
    """
    queryset = Chatroom.objects.all()
    serializer_class = serializers.ChatroomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsReviewOwnerOrReadOnly)
