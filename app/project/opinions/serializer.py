from rest_framework import serializers
from .models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    # user = ReviewSerializer(
    #     required=False,
    # )
    class Meta:
        model = Opinion
        fields = ['helpful', 'awesome', 'random']
        # read_only_fields = ['helpful', 'awesome', 'random']
