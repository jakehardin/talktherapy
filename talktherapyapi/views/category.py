"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from talktherapyapi.models import Category

class CategoryView(ViewSet):
    """Closet Share cateogry view"""

    def retrieve(self, request, pk):
        
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all category

        Returns:
            Response -- JSON serialized list of category
        """
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def create(self, request):
        """Handle GET requests for single Category
        Returns:
            Response -- JSON serialized Category
        """

        category = Category.objects.create(
            label=request.data["label"],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """
    
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.description = request.data["description"]
        category.save()
        
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        
        category = Category.objects.get(pk=pk)
        category.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # def popular_genres(self, request):
    #     """
    #     Retrieve a list of popular genres based on the number of songs associated with each genre
    #     """
        
    #     genres = Genre.objects.annotate(song_count=Count('songs')).order_by('-song_count')[:1]

    #     serializer = SongsgitGenreSerializer(genres, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label', 'description')
