from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReviewSerializer
from .models import Review
from .permissions import IsOwnerOrReadOnly


class CreateReviewView(GenericAPIView):
    """
            Create new review
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        data = {
            **request.data,
            'restaurant': kwargs['pk'],
        }
        serializer = self.serializer_class(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            instance = serializer.create(serializer.validated_data)
            return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)


class GetReviewListView(APIView):
    """
            Get the list of the reviews for a single restaurant
    """
    serializer_class = ReviewSerializer

    def get(self, request, pk, **kwargs):
        reviews = Review.objects.filter(restaurant__id=pk)
        response = self.serializer_class(reviews, many=True).data
        return Response(response)


class GetUserReviewListView(APIView):
    """
            Get the list of the reviews by a single user.
    """
    serializer_class = ReviewSerializer

    def get(self, request, pk, **kwargs):
        reviews = Review.objects.filter(user__id=pk)
        response = self.serializer_class(reviews, many=True).data
        return Response(response)


class GetUpdateDeleteReviewView(RetrieveUpdateDestroyAPIView):
    """
            Get, Delete, Update a review on restaurant by id (only by owner)
    """

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]


class ListReviewsGetOpinionByCurrentUserView(ListAPIView):
    """
             List of all reviews get opinion by current user
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(opinions__user=self.request.user)
