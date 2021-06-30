from django.contrib import admin

from book.models import BookReview, Comment, Favorites

admin.site.register(BookReview)
admin.site.register(Comment)
admin.site.register(Favorites)