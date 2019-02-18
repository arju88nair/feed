
from rest_framework import generics,viewsets

from .models import Doctor,Interactions
from .serializers import DoctorSerializer,InteractionsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings



class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('location', 'speciality')


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




@api_view(["POST"])
def search_doctors(request):
    try:
        liked=Interactions.objects.filter(
        user_id=1).filter(doctor_id=1)       

        data = list(liked.values())
        return JsonResponse({"success":True,"data":data}, safe=False)       
    
        if request.user.is_authenticated:
            liked=Interactions.objects.filter(
    user_id=1
)           
            
        else:
            return JsonResponse("Lorem ipsum blah",safe=False)


        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
