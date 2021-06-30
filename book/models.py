from django.db import models
from django.conf import settings

from category.models import Category
from user.models import CustomUser


class BookReview(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(blank=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='reviews',)
    preview = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_author = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.owner}-->{self.title}"


class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    review = models.ForeignKey(BookReview, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner}->{self.review}->{self.created_at}-{self.body[0:10]}"
