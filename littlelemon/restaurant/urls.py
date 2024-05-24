from django.urls import path
from .views import menuview,bookingview, index

urlpatterns = [
    path('', index, name='index'),
    path('menu/',menuview.as_view()),
    path('booking/', bookingview.as_view()),

]