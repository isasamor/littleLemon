from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking
from .serializer import bookingSerializer, menuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class bookingview(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializers = bookingSerializer(items,many=True)
        return Response(serializers.data) # Return JSON

class menuview(APIView):
    def post(self,request):
        serializer = menuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":"serialized.data"})
            
