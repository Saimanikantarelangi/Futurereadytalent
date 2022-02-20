from django.db import models

class Flight(models.Model):
        flightid=models.IntegerField()


        destination= models.CharField(max_length=40)
        distance = models.IntegerField()
        fuelquantity = models.IntegerField()
