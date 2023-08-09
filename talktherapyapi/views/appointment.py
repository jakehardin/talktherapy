"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from talktherapyapi.models import Category, Appointment, User, Therapist

class AppointmentView(ViewSet):
    """Closet Share appointment view"""

    def retrieve(self, request, pk):
        
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Appointment

        Returns:
            Response -- JSON serialized list of appointment
        """
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def create(self, request):
        """Handle POST requests to create a new Appointment
        Returns:
            Response -- JSON serialized Appointment
        """
        print("Received request data:", request.data)

        category_id = request.data["category_id"]
        therapist_id = request.data["therapist_id"]
        user_id = request.data["user"]

        print("category_id:", category_id)
        print("therapist_id:", therapist_id)
        print("user_id:", user_id)

        try:
            category = Category.objects.get(id=category_id)
            therapist = Therapist.objects.get(id=therapist_id)
            user = User.objects.get(id=user_id)

            appointment = Appointment.objects.create(
                user=user,
                therapist_id=therapist,
                category_id=category,
                service=request.data["service"],
                day=request.data["day"],
                time=request.data["time"],
                time_ordered=request.data["time_ordered"],
            )
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Category.DoesNotExist as category_error:
            return Response({'message': f"Category not found: {category_error}"}, status=status.HTTP_400_BAD_REQUEST)
        except Therapist.DoesNotExist as therapist_error:
            return Response({'message': f"Therapist not found: {therapist_error}"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as user_error:
            return Response({'message': f"User not found: {user_error}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def create(self, request):
    #     """Handle GET requests for single Appointment
    #     Returns:
    #         Response -- JSON serialized Appointment
    #     """

    #     category = Category.objects.get(pk=request.data["category_id"])
    #     therapist = Therapist.objects.get(pk=request.data["therapist_id"])
    #     patient = User.objects.get(pk=request.data["user"])


    #     appointment = Appointment.objects.create(
    #         user=patient,
    #         therapist_id=therapist,
    #         category_id=category,
    #         service=request.data["service"],
    #         day=request.data["day"],
    #         time=request.data["time"],
    #         time_ordered=request.data["time_ordered"],
    #     )
    #     serializer = AppointmentSerializer(appointment)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for an appointment

        Returns:
            Response -- Empty body with 204 status code
        """
    
        appointment = Appointment.objects.get(pk=pk)
        category_id = Category.objects.get(pk=request.data["category_id"])
        appointment.category_id = category_id
        therapist_id = Therapist.objects.get(pk=request.data["therapist_id"])
        appointment.therapist_id = therapist_id
        user = User.objects.get(pk=request.data["user"])
        appointment.user = user
        appointment.service = request.data["service"]
        appointment.day = request.data["day"]
        appointment.time = request.data["time"]
        appointment.time_ordered = request.data["time_ordered"]
        
        appointment.save()
        
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        
        appointment = Appointment.objects.get(pk=pk)
        appointment.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Appointment
        fields = ('id', 'user', 'therapist_id', 'category_id', 'service', 'day', 'time', 'time_ordered')
