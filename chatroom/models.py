from django.db import models

from bookreview_project import settings


class Chatroom(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chatroom', on_delete=models.CASCADE)
    chat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.chat_name


class Messages(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, related_name='messages', on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}->{self.chatroom}"
