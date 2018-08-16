from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    # number_of_reviews = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'category',
            'country',
            'street',
            'city',
            'ZIP',
            'website',
            'phone',
            'image',
            'credit_card',
            'take_reservation',
            'user',
            'rating',
            'kids_menu',
            # 'number_of_reviews',
        ]
        read_only_fields = ['id', 'user']

    def get_rating(self, restaurant):
        reviews = restaurant.reviews.all()
        avg_of_rating = 0
        if reviews:
            sum_of_rating = 0
            for review in reviews:
                sum_of_rating += review.rating
            avg_of_rating = sum_of_rating / len(reviews)
        return avg_of_rating

    #
    #     def get_number_of_reviews(self, restaurant):
    #         return len(restaurant.reviews.all())
    #
    def get_image(self, restaurant):
        if restaurant.image:
            return restaurant.image.url
        return "Nope"

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data, user=self.context.get('request').user)


class RestaurantCategroySerializer(serializers.Serializer):
    name = serializers.CharField()
