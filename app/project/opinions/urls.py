from django.urls import path

from ..opinions.views import GetCreateHelpfulOpinionView, GetCreateAwesomeOpinionView, GetCreateRandomOpinionView

app_name = 'opinions'  # backend/api/opinions/

urlpatterns = [
    path('helpful/<int:pk>/', GetCreateHelpfulOpinionView.as_view(), name='toggle_helpful_opinion'),
    path('awesome/<int:pk>/', GetCreateAwesomeOpinionView.as_view(), name='toggle_awesome_opinion'),
    path('random/<int:pk>/', GetCreateRandomOpinionView.as_view(), name='toggle_random_opinion'),
    #path('helpfuls/<int:review_id>', GetHelpfulOpinionsListView.as_view(), name='get_helpful_opinions'),

]

