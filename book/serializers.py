from rest_framework import serializers

from django.db.models import Avg
from book.models import BookReview, Comment

from book.models import BookReview, Comment, Favorites
from category.serializers import CategorySerializer
from like.models import Like


# class BookImageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = BookReview
#         exclude = ('id', )
from like.serializers import LikeSerializer
from rating.models import Mark


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'review')


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = BookReview
        fields = ('id', 'title', 'book_author',
                  'review',  'owner',
                  'category', 'preview', 'image', 'comments')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(many=False, instance=instance.category).data
        representation['like'] = instance.review_likes.filter(like=True).count()
        representation['mark'] = instance.mark.aggregate(Avg('mark'))
        return representation


class FavoritesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorites
        fields = ('review', 'favorites', 'owner',)