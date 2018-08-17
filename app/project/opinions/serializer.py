from rest_framework import serializers

from ..review.serializers import ReviewSerializer
from .models import Opinion


class OpinionSerializer(serializers.ModelSerializer):

    # user = ReviewSerializer(
    #     required=False,
    # )


    class Meta:
        model = Opinion
        fields = ['helpful', 'awesome', 'random']
        # read_only_fields = ['helpful', 'awesome', 'random']

    # def update(self, instance, validated_data):
    #     instance.things_i_love = validated_data.get('things_i_love', instance.things_i_love)
    #     instance.save()
    #     return instance
