from django.contrib import admin

from book.models import BookReview, BookImages

admin.site.register(BookReview)
admin.site.register(BookImages)
