from django.db import models


class Category(models.Model):
    name = models.SlugField(max_length=150, primary_key=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
