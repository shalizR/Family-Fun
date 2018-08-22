# from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from ..restaurant.serializers import RestaurantSerializer
from ..restaurant.models import Restaurant


class RestaurantSearchView(APIView):
    serializer_class = RestaurantSerializer

    def post(self, request, **kwargs):
        category = kwargs.get('category')
        q = request.query_params.get('search_string')
        restaurants = Restaurant.objects.filter(category=category).filter(name__icontains=q)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class FastFoodSearchView(APIView):
    serializer_class = RestaurantSerializer

    def post(self, request, **kwargs):
        # data = request.data
        q = request.query_params.get('search_string')
        restaurants = Restaurant.objects.filter(name__icontains=q, category='fast_food')
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class CafeSearchView(APIView):
    serializer_class = RestaurantSerializer

    def post(self, request, **kwargs):
        # data = request.data
        q = request.query_params.get('search_string')
        restaurants = Restaurant.objects.filter(name__icontains=q, category='cafe')
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
