from rest_framework import generics, viewsets, permissions
from .models import Booking, Menu
from .serializer import bookingSerializer, menuSerializer
from rest_framework.decorators import permission_classes


@permission_classes([permissions.IsAuthenticated])
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    #permission_classes = [permissions.IsAuthenticated]

class SingelMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 







# class bookingview(APIView):
#     def get(self,request):
#         items = Booking.objects.all()
#         serializers = bookingSerializer(items,many=True)
#         return Response(serializers.data) # Return JSON

# class menuview(APIView):
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data":"serialized.data"})

