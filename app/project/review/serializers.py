from rest_framework import serializers

from project.opinions.serializer import OpinionSerializer
from ..review.models import Review
from ..user_profile.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(
        required=False,
    )
    opinions = OpinionSerializer(
        required=False,
        many=True,
    )

    class Meta:
        model = Review
        fields = [
            'id',
            'content',
            'date_created',
            'date_modified',
            'user',
            'restaurant',
            'has_changing_table',
            'place_for_stroller',
            'isNoisy',
            'friendly_waiting_staff',
            'high_chair',
            'are_there_steps',
            'rating',
            'has_tablecloth',
            'has_quick_service',
            'price_level',
            'opinions',
        ]
        read_only_fields = [
            'id',
            'date_created',
            'date_modified',
            'user',
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
