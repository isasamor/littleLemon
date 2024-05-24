from rest_framework import generics, viewsets, permissions
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer
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
