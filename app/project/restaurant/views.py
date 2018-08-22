from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..review.permissions import IsOwnerOrReadOnly
from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantCategroySerializer


class CreateRestaurantView(generics.GenericAPIView):
    """
        Create a new restaurant
    """
    serializer_class = RestaurantSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        post = serializer.create(serializer.validated_data)
        return Response(RestaurantSerializer(post).data)


class RestaurantsListView(generics.ListAPIView):
    """
        Get list of restaurants
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantCategoriesListView(APIView):
    """
        List all restaurants categories
    """
    serializer_class = RestaurantCategroySerializer

    def get(self, request, *args, **kwargs):
        categories = map(lambda x: {'name': x[1], 'key': x[0]}, Restaurant.CATEGORIES)
        return Response(self.serializer_class(categories, many=True).data)


class GetUpdateDeleteRestaurantByIDView(RetrieveUpdateDestroyAPIView):
    """
            Get, Delete, Update a restaurant by id (only by owner)
    """

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]


class ListRestaurantsByCategoryView(ListAPIView):
    """
        List all restaurants based on categories (restaurant, fast_food, cafe)
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(category=self.kwargs['category'])


class ListRestaurantsByUser(ListAPIView):
    """
        Lists all restaurants created by a specific user
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.kwargs['user_id'])


class ListRestaurantsWithKidsMenuView(generics.GenericAPIView):
    """
        Lists all restaurants with kids menu
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get(self, request, **kwargs):
        restaurants = Restaurant.objects.filter(kids_menu=True)
        response = self.serializer_class(restaurants, many=True).data
        return Response(response)


class ListRestaurantsWithReservation(generics.GenericAPIView):
    """
        Lists all restaurants with reservation
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get(self, request, **kwargs):
        restaurants = Restaurant.objects.filter(take_reservation=True)
        response = self.serializer_class(restaurants, many=True).data
        return Response(response)
