from django.contrib import admin

from .opinions.models import Opinion
from .restaurant.models import Restaurant
from .review.models import Review
from .user_profile.models import UserProfile


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'rating', 'user', 'restaurant']
    search_fields = ['content']


# @admin.register(Likes)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'id', 'review']
#     search_fields = ['review', 'user']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'category', 'kids_menu']
    search_fields = ['name']


@admin.register(UserProfile)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'profile_pic']


@admin.register(Opinion)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'review', 'helpful', 'awesome', 'random']
    # search_fields = ['content']
