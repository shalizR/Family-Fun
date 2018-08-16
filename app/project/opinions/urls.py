from django.urls import path

from ..opinions.views import GetCreateHelpfulOpinionView, GetCreateAwesomeOpinionView, GetCreateRandomOpinionView

app_name = 'opinions'  # backend/api/opinions/

urlpatterns = [
    path('helpful/<int:pk>/', GetCreateHelpfulOpinionView.as_view(), name='toggle_helpful_opinion'),
    path('awesome/<int:pk>/', GetCreateAwesomeOpinionView.as_view(), name='toggle_awesome_opinion'),
    path('random/<int:pk>/', GetCreateRandomOpinionView.as_view(), name='toggle_random_opinion'),
    # path('reviews/helpful/', ListHelpfulOpinionView.as_view(), name='helpfuls'),
    # path('reviews/helpful/', ListAwesomeOpinionView.as_view(), name='awesomes'),
    # path('reviews/helpful/', ListRandomOpinionView.as_view(), name='randoms'),
]
