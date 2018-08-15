from django.urls import path

from .views import CreateReviewView, GetReviewListView, GetUserReviewListView, GetUpdateDeleteReviewView

app_name = 'review'

urlpatterns = [
    path('new/<int:pk>/', CreateReviewView.as_view(), name='new_review'),
    path('restaurant/<int:pk>/', GetReviewListView.as_view(), name='review_list'),
    path('user/<int:pk>/', GetUserReviewListView.as_view(), name='list_of_reviews_of_user'),
    path('<int:pk>/', GetUpdateDeleteReviewView.as_view(), name='get_post_delete_review_by_id'),
    # path('like/<int:pk>/', CreateDeleteLikeView.as_view(), name='like_review'),
    # path('likes/', ListLikedView.as_view(), name='likes'),
    # path('comments/', ListCommentedReviewsdView.as_view(), name='reviews_current_user_commented'),

]
