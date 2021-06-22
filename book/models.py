from django.db import models
from django.conf import settings

from category.models import Category


class BookReview(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(blank=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='reviews', null=True)
    preview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_author = models.CharField(max_length=255, null=True)


    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.owner}-->{self.title}"


class BookImages(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    review = models.ForeignKey(BookReview, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return "image" + str(random.randint(111111, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(BookImages, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -> {self.review.id}"


