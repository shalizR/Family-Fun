from django.urls import path
from .views import UserProfileView, ListUsersView, UserBySearchView, UserByIdView, UpdateUserProfileView

app_name = 'users'  # backend/api/users/
urlpatterns = [
    path('me/', UserProfileView.as_view(), name='get_user_profile'),
    path('me/update/', UpdateUserProfileView.as_view(), name='update_userprofile'),
    path('list/', ListUsersView.as_view(), name='list_all_users'),
    path('search/', UserBySearchView.as_view(), name='user_by_search'),
    path('<int:user_id>/', UserByIdView.as_view(), name='user_by_id'),
]
