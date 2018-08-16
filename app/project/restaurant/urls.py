from django.urls import path

from .views import RestaurantsListView, RestaurantCategoriesListView, GetUpdateDeleteRestaurantByIDView, \
    CreateRestaurantView, ListRestaurantsByCategoryView, ListRestaurantsByUser

app_name = 'restaurants'  # backend/api/restaurants/

urlpatterns = [

    path('new/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('', RestaurantsListView.as_view(), name='restaurants_list'),
    path('<int:pk>/', GetUpdateDeleteRestaurantByIDView.as_view(), name='get_create_delete_restaurant_by_id'),
    path('categories/', RestaurantCategoriesListView.as_view(), name='list_all_categories'),
    path('category/<str:category>/', ListRestaurantsByCategoryView.as_view(), name='get_restaurants_by_category'),
    path('user/<int:user_id>/', ListRestaurantsByUser.as_view(), name='list_restaurants_created_by_user'),
]
