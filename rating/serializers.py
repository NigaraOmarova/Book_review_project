from rest_framework import serializers

from rating.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Mark
        fields = ['book', 'mark', 'owner']