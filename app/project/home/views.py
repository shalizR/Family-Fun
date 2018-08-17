from rest_framework.generics import ListAPIView
from ..restaurant.models import Restaurant
from ..restaurant.serializers import RestaurantSerializer


class HomeView(ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        restaurants = list(Restaurant.objects.all())

        restaurant_scores = []
        res = []

        for restaurant in restaurants:
            reviews = list(restaurant.reviews.all())
            scores = [review.rating for review in reviews]
            if len(scores) == 0:
                restaurant_scores += [0]
            else:
                score_mean = sum(scores) / len(scores)
                restaurant_scores += [score_mean]

        for _ in range(4):
            max_score = max(restaurant_scores)
            index = restaurant_scores.index(max_score)
            restaurant = restaurants[index]
            res += [restaurant]
            restaurant_scores[index] = -1

        return res
