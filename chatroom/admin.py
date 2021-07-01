from django.contrib import admin

from chatroom.models import Chatroom, Messages

admin.site.register(Chatroom)
admin.site.register(Messages)
