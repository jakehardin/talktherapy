"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from talktherapyapi.models import Therapist, Category


class TherapistView(ViewSet):
    """DOCSTRING
    """

    def retrieve(self, request, pk):
        """DOCSTRING
        """
        therapist = Therapist.objects.get(pk=pk)
        serializer = TherapistSerializer(therapist)
        return Response(serializer.data)


    def list(self, request):
        """DOCSTRING
        """
        therapists = Therapist.objects.all()
        serializer = TherapistSerializer(therapists, many=True)
        return Response(serializer.data)

    def create(self, request):
        """DOCSTRING
        """
        category = Category.objects.get(pk=request.data["categoryId"])

        therapist = Therapist.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            category_id=category,
            created_on=request.data["created_on"],
            profile_image_url=request.data["profile_image_url"],
            description=request.data["description"],
            website=request.data["website"],
            contact=request.data["contact"],
            favorite=request.data["favorite"],
            city=request.data["city"],
            state=request.data["state"],
        )
        serializer = TherapistSerializer(therapist)
        return Response(serializer.data)

    def update(self, request, pk):
        """DOCSTRING
        """

        product = Product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.price = request.data["price"]
        product.image = request.data["image"]

        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TherapistSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Therapist
        fields = ('id', 'first_name', 'last_name', 'category_id', 'created_on', 'profile_image_url', 'description', 'website', 'contact', 'favorite', 'city', 'state' )
