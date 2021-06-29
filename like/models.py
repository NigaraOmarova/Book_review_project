from django.db import models

from book.models import BookReview
from user.models import CustomUser


class Like(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner_likes')
    book = models.ForeignKey(BookReview, on_delete=models.CASCADE, related_name='review_likes')
    like = models.BooleanField()

    class Meta:
        unique_together = ['owner', 'book']