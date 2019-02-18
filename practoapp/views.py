
from rest_framework import generics

from .models import Doctor,Interactions
from .serializers import DoctorSerializer,InteractionsSerializer
from django_filters.rest_framework import DjangoFilterBackend




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


class InteractionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interactions.objects.all()
    serializer_class = InteractionsSerializer

