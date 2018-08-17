from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from ..user_profile.serializers import UserSerializer
from ..review.serializers import ReviewSerializer
from ..review.models import Review
from ..restaurant.serializers import RestaurantSerializer
from ..restaurant.models import Restaurant


User = get_user_model()


class SearchView(APIView):

    def post(self, request, **kwargs):
        data = request.data
        type = data.get('type')
        search_string = data.get('search_string')
        category = data.get('category')

        if type == 'restaurants':
            if category is None:
                restaurants = Restaurant.objects.filter(name__icontains=search_string)
            else:
                restaurants = Restaurant.objects.filter(name__icontains=search_string, category=category)
            serializer = RestaurantSerializer(instance=restaurants, many=True)
            return Response(serializer.data)
        elif type == 'reviews':
            if category is None:
                reviews = Review.objects.filter(content__icontains=search_string)
            else:
                reviews = Review.objects.filter(content__icontains=search_string, restaurant__category=category)
            serializer = ReviewSerializer(instance=reviews, many=True)
            return Response(serializer.data)
        elif type == 'users':
            users = User.objects.filter(username__icontains=search_string)
            serializer = UserSerializer(instance=users, many=True)
            return Response(serializer.data)
