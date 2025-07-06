from django.db import models


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}' 

class Booking(models.Model):
    name = models.CharField(max_length=255, null=True)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.name} : {str(self.booking_date)}'