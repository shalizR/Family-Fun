from django.urls import path

from ..opinions.views import GetCreateHelpfulOpinionView

app_name = 'opinions'

urlpatterns = [
    path('helpful/<int:pk>/', GetCreateHelpfulOpinionView.as_view(), name='helpful_opinion'),
    # path('awesome/<int:pk>/', GetCreateAwesomeOpinionView.as_view(), name='awesome_opinion'),
    # path('random/<int:pk>/', GetCreateRandomOpinionView.as_view(), name='random_opinion'),
    # path('reviews/helpful/', ListHelpfulOpinionView.as_view(), name='helpfuls'),
    # path('reviews/helpful/', ListAwesomeOpinionView.as_view(), name='awesomes'),
    # path('reviews/helpful/', ListRandomOpinionView.as_view(), name='randoms'),
]


