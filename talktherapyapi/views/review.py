"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from talktherapyapi.models import Therapist, User, Review


class ReviewView(ViewSet):
    """DOCSTRING
    """

    def retrieve(self, request, pk):
        """DOCSTRING
        """
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


    def list(self, request):
        """DOCSTRING
        """
        reviews = Review.objects.all()

        therapist_id = request.query_params.get('therapist_id', None)
        if therapist_id is not None:
            reviews = reviews.filter(therapist_id_id=therapist_id)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """DOCSTRING
        """
        therapist = Therapist.objects.get(id=request.data["therapist_id"])
        reviewer = User.objects.get(id=request.data["reviewer_id"])

        review = Review.objects.create(
            therapist_id=therapist,
            reviewer_id=reviewer,
            created_on=request.data["created_on"],
            content=request.data["content"],
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update(self, request, pk):
        """DOCSTRING
        """

        review = Review.objects.get(pk=pk)
        review.content = request.data["content"]

        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DOCTSTRING
        """
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Review
        fields = ('id', 'therapist_id',
                  'reviewer_id', 'content', 'created_on' )
        