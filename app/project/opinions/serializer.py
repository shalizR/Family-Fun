from rest_framework import serializers
from .models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    # user = ReviewSerializer(
    #     required=False,
    # )
    class Meta:
        model = Opinion
        fields = ['id', 'helpful', 'awesome', 'random', 'user']
        # read_only_fields = ['helpful', 'awesome', 'random']
