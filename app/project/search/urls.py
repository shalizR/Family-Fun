from django.urls import path

from .views import RestaurantSearchView, FastFoodSearchView, CafeSearchView

app_name = 'search'  # backend/api/search/
urlpatterns = [
    # path('', RestaurantSearchView.as_view(), name='search'),
    path('<str:category>/', RestaurantSearchView.as_view(), name='search_restaurants'),
    path('restaurants/', RestaurantSearchView.as_view(), name='search_restaurants'),
    path('fast_foods/', FastFoodSearchView.as_view(), name='search_fast_foods'),
    path('cafes/', CafeSearchView.as_view(), name='search_cafes'),

]
