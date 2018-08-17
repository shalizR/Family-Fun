from rest_framework import serializers

# from ..restaurant.serializers import RestaurantSerializer
from ..review.models import Review
from ..user_profile.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(
        required=False,
    )
    # restaurant = RestaurantSerializer(
    #     required=True,
    # )

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
        ]
        read_only_fields = [
            'id',
            'date_created',
            'date_modified',
            'user',
        ]

    # def get_likes_count(self, post):
    #     return post.likes.count()

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
    # def create(self, validated_data):
    #     return Review.objects.create(
    #         **validated_data,
    #     )
