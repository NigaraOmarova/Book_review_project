from django.db import models

from book.models import BookReview
from user.models import CustomUser


class Mark(models.Model):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    choose_your_mark = [
        (one, 'Ну такое себе'),
        (two, 'Ничего так'),
        (three, 'Нормульно'),
        (four, 'Хорошо'),
        (five, 'Классно!')
    ]


class Mark(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner_mark')
    book = models.ForeignKey(BookReview, on_delete=models.CASCADE, related_name='mark')
    mark = models.PositiveIntegerField(choices=Mark.choose_your_mark)

    def __str__(self):
        return f'{self.owner} --> {self.book} --> {self.mark}'

    class Meta:
        unique_together = ('book', 'owner')
