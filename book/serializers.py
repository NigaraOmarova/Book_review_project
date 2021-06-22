from rest_framework import serializers

from book.models import BookReview
from category.serializers import CategorySerializer


class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookReview
        exclude = ('id', )


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    images = BookImageSerializer(many=True, required=False)

    class Meta:
        model = BookReview
        fields = ('id', 'title', 'book_author',
                  'review',  'owner', 'comments',
                  'category', 'preview', 'images')


