"""View module for handling requests about game types"""
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

        category_id = request.query_params.get('category_id', None)
        if category_id is not None:
            therapists = therapists.filter(category_id_id=category_id)

        favorite = request.query_params.get('favorite', False)
        if favorite is not False:
            therapists = therapists.filter(favorite=True)

        serializer = TherapistSerializer(therapists, many=True)
        return Response(serializer.data)

    def create(self, request):
        """DOCSTRING
        """
        category_id = Category.objects.get(id=request.data["category_id"])

        therapist = Therapist.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            category_id=category_id,
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

        therapist = Therapist.objects.get(pk=pk)
        therapist.first_name = request.data["first_name"]
        therapist.last_name = request.data["last_name"]
        therapist.profile_image_url = request.data["profile_image_url"]
        therapist.description = request.data["description"]
        therapist.website = request.data["website"]
        therapist.contact = request.data["contact"]
        therapist.favorite = request.data["favorite"]
        therapist.city = request.data["city"]
        therapist.state = request.data["state"]
        
        category_id = Category.objects.get(pk=request.data["category_id"])
        therapist.category_id = category_id

        therapist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DOCTSTRING
        """
        therapist = Therapist.objects.get(pk=pk)
        therapist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def search(self, request):
        """Search therapists by first name, last name, city, or state, """

        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        city = request.query_params.get('city', None)
        state = request.query_params.get('state', None)

        therapists = Therapist.objects.all()

        if first_name:
            therapists = therapists.filter(first_name__icontains=first_name)
        if last_name:
            therapists = therapists.filter(last_name__icontains=last_name)
        if city:
            therapists = therapists.filter(city__icontains=city)
        if state:
            therapists = therapists.filter(state__icontains=state)

        serializer = TherapistSerializer(therapists, many=True)
        return Response(serializer.data)

class TherapistSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Therapist
        fields = ('id', 'first_name',
                  'last_name', 'category_id',
                  'created_on', 'profile_image_url',
                  'description', 'website', 'contact',
                  'favorite', 'city', 'state' )
        