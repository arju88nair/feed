from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('title', 'name', 'summary', 'location',
            'gender', 'speciality',
            'created_date', 'published_date')
        model = models.Doctor



class InteractionsSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('user_id', 'doctor_id', 'count')
        model = models.Interactions