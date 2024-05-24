from django.urls import path
from .views import MenuItemView, SingelMenuItemView

urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingelMenuItemView.as_view()),
    #path('booking/', bookingview.as_view()),

]