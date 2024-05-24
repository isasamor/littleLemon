# serialize: to serialize to model data to json/xml
from .models import Booking,Menu
from rest_framework import serializers

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        