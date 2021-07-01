from rest_framework import serializers
from chatroom.models import Messages, Chatroom


class MessagesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Messages
        fields = ('owner', 'body', 'chatroom')


class MessagesChatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Messages
        fields = ('owner', 'body',)


class ChatroomSerializer(serializers.ModelSerializer):
    messages = MessagesChatSerializer(many=True, read_only=True)

    class Meta:
        model = Chatroom
        fields = ('id', 'chat_name', 'messages')
