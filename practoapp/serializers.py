from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('title', 'name', 'summary', 'location',
            'gender', 'speciality',
            'created_date', 'published_date','is_active')
        model = models.Doctor



class InteractionsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_id', 'doctor_id', 'is_liked')
        model = models.Interactions



class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('doctor_id', 'availability')
        model = models.Availability