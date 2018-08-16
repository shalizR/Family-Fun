from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
            # something = opinion.helpful
            # serializer = OpinionSerializer(data={"helpful": something})
            # if serializer.is_valid():
            opinion.save()
            return Response('OK')
        except Opinion.DoesNotExist:
            print('The review is not exist!')
    # serializer_class = OpinionSerializer
    # def get(self, request, pk, **kwargs):
    #     opinion = Opinion.objects.get(review=pk)
    #     opinion.helpful = not opinion.helpful
    #     response = self.serializer_class(posts, many=True).data
    #     return Response(response)
    # def post(self, request, **kwargs):
    #     helpful, created = Opinion.objects.get_or_create(review=request.user)
    #     helpful = not helpful


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
            return Response('OK')
        except Opinion.DoesNotExist:
            print('The review is not exist!')


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
            return Response('OK')
        except Opinion.DoesNotExist:
            print('The review is not exist!')

# class ListHelpfulOpinionView(ListAPIView): (Move to review view)
#     """
#             Get the list of the helpful opinion for a single review
#     """
#     serializer_class = OpinionSerializer
#
#     def get(self, request, pk, **kwargs):
#         opinions = Opinion.objects.filter(review=pk)
#         response = self.serializer_class(reviews, many=True).data
#         return Response(response)
