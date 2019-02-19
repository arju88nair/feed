
from rest_framework import generics,viewsets

from .models import Doctor,Interactions,Availability
from .serializers import DoctorSerializer,InteractionsSerializer,AvailabilitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings


## TODO: Should rely on the token based authentication

## Generic views for all the 3 models
class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('location', 'speciality','gender')

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer



class InteractionsList(generics.ListCreateAPIView):
    queryset = Interactions.objects.all()
    serializer_class = InteractionsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id', 'doctor_id')
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class InteractionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interactions.objects.all()
    serializer_class = InteractionsSerializer


class AvailabilityList(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('doctor_id', 'availability')


class AvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer



"""[For liking/un-liking a specific post]

Returns:
    [JSON] -- [Return json response]
"""

@api_view(["POST"])
def addlike(request):
    ## Checks if the user is authenticated or not
    if request.user.is_authenticated:
        try:
            doctor=request.POST['doctor_id']
            user_id=request.user.id
            ## Checking if the doctor is present for the requested id
            doctors=Doctor.objects.filter(pk=doctor)
            if(doctors):
                ## Getting the interaction for the logged in user and doctor id
                liked=Interactions.objects.filter(
            user_id=user_id).filter(doctor_id=doctor) 
            ## Updating or creating based on the response 
            ## TODO : Should rely on the update_create method on the django model and move the toggling of the is_liked to serializer
                if(liked):
                    for like in liked:
                        like.user_id = not like.user_id
                        like.save()   
                else:
                    Interactions.objects.create(user_id=user_id, doctor_id=doctor ,is_liked=True)
                return JsonResponse({"success":True,"message":"Successfully liked"}, safe=False)        
            else:
                return Response("Doctor doesn't exist",status.HTTP_400_BAD_REQUEST)    

        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

    else:
        return Response("User is not authenticated",status.HTTP_400_BAD_REQUEST)
    

        
