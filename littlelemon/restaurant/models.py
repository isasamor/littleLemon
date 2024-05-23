from django.db import models

# Create your models here.
class Booking(models.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return super().__str__()


class Menu(models.Model):
    #id = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return super().__str__()

