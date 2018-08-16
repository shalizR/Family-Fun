from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

User = get_user_model()


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, userprofile):
        return userprofile.user.username

    class Meta:
        model = UserProfile
        fields = ['username', 'location', 'phone', 'joined_date', 'profile_pic']
        read_only_fields = ['username']

    # def update(self, instance, validated_data):
    #     instance.things_i_love = validated_data.get('things_i_love', instance.things_i_love)
    #     instance.save()
    #     return instance


class UserSerializer(serializers.ModelSerializer):

    location = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    joined_date = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'location', 'phone', 'joined_date', 'profile_pic']
        read_only_fields = fields

    def get_location(self, user):
        return user.user_profile.location

    def get_phone(self, user):
        return user.user_profile.phone

    def get_joined_date(self, user):
        return user.user_profile.joined_date

    def get_profile_pic(self, user):
        if user.user_profile.profile_pic:
            return user.user_profile.profile_pic.url
        return "Nope"
