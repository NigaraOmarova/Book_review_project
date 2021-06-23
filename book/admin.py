from django.contrib import admin

from book.models import BookReview, Comment

admin.site.register(BookReview)
admin.site.register(Comment)
