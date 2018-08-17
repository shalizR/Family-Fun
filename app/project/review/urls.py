from django.urls import path

from .views import CreateReviewView, GetReviewListView, GetUserReviewListView, GetUpdateDeleteReviewView, \
    ListReviewsGetOpinionByCurrentUserView

app_name = 'review'  # backend/api/reviews/

urlpatterns = [
    path('new/<int:pk>/', CreateReviewView.as_view(), name='new_review'),
    path('restaurant/<int:pk>/', GetReviewListView.as_view(), name='review_list'),
    path('user/<int:pk>/', GetUserReviewListView.as_view(), name='list_reviews_of_user'),
    path('<int:pk>/', GetUpdateDeleteReviewView.as_view(), name='get_update_delete_review_by_id'),
    path('opinions/', ListReviewsGetOpinionByCurrentUserView.as_view(), name='list_reviews_get_opinion_by_a_user'),
]
