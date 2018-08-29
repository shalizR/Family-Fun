from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from ..review.models import Review
from ..review.models import Review
from ..review.permissions import AllowedToMakeOpinion
from .models import Opinion
from .serializer import OpinionSerializer


class GetCreateHelpfulOpinionView(APIView):

    """
            Create or get an opinion (helpful)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise NotFound
        opinion, created = Opinion.objects.get_or_create(review=review, user=request.user)
        if created:
            opinion.helpful = True
        else:
            opinion.helpful = not opinion.helpful
        opinion.save()
        return Response(OpinionSerializer(opinion).data)


class GetCreateAwesomeOpinionView(APIView):
    """
            Create or get an opinion (awesome)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise NotFound
        opinion, created = Opinion.objects.get_or_create(review=review, user=request.user)
        if created:
            opinion.awesome = True
        else:
            opinion.awesome = not opinion.helpful
        opinion.save()
        return Response(OpinionSerializer(opinion).data)


class GetCreateRandomOpinionView(APIView):
    """
            Create or get an opinion (random)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise NotFound
        opinion, created = Opinion.objects.get_or_create(review=review, user=request.user)
        if created:
            opinion.helpful = True
        else:
            opinion.random = not opinion.random
        opinion.save()
        return Response(OpinionSerializer(opinion).data)

# class GetHelpfulOpinionsListView(ListAPIView):
#     """
#             Get the list of all helpful opinions on a single review
#     """
#     serializer_class = OpinionSerializer
#
#     def get(self, request, review_id, **kwargs):
#         opinions = Opinion.objects.filter(review=review_id, helpful=True)
#         response = self.serializer_class(opinions, many=True).data
#         return Response(response)
