# serialize: to serialize to model data to json/xml
from .models import Booking,Menu
from rest_framework import serializers
from django.contrib.auth.models import User

# ModelSerializer is a special type of serializer that quickly creates a serializer class from the Django model fields.
# The ModelSerializer class is declared in the rest_framework.serializers module.

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# User objects are the core of the authentication system. They typically represent the people interacting
#  with your site and are used to enable things like restricting access, registering user profiles,
#  associating content with creators etc
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
