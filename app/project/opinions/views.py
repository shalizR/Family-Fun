from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from ..review.models import Review
from ..review.permissions import AllowedToMakeOpinion
from .models import Opinion
# from .serializer import OpinionSerializer


class GetCreateHelpfulOpinionView(APIView):

    """
            Create an opinion (helpful)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):

        try:
            opinion = Opinion.objects.get(review=pk)
            opinion.helpful = not opinion.helpful
            opinion.save()
        except Opinion.DoesNotExist:
            raise NotFound
        return Response('OK')


class GetCreateAwesomeOpinionView(APIView):
    """
            Create an opinion (awesome)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):

        try:
            opinion = Opinion.objects.get(review=pk)
            opinion.awesome = not opinion.awesome
            opinion.save()
        except Opinion.DoesNotExist:
            raise NotFound
        return Response('OK')


class GetCreateRandomOpinionView(APIView):
    """
            Create an opinion (random)
    """
    permission_classes = [IsAuthenticated, AllowedToMakeOpinion]

    def get(self, request, pk, **kwargs):

        try:
            opinion = Opinion.objects.get(review=pk)
            opinion.random = not opinion.random
            opinion.save()
        except Opinion.DoesNotExist:
            raise NotFound
        return Response('OK')

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
