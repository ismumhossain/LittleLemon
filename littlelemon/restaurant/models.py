from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    number_of_guests = models.IntegerField(default=10, null=False)
    bookingdate = models.DateField()

    def __str__(self): 
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'