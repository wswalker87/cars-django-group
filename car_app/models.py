from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.EmailField(max_length=255)

class CarModel(models.Model):
    make = models.CharField(max_length=255, unique=True)
    model = models.CharField(max_length=255, unique=True)

class Car(models.Model):
    number_of_owners = models.IntegerField(default=1)
    registration_number = models.CharField(max_length=255)
    manufacture_year = models.IntegerField()
    number_of_doors = models.IntegerField(default=4)
    mileage = models.IntegerField()
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

class Advertisement(models.Model):
    advertisement_date = models.DateField(auto_now_add=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

class UserProfiles(models.Model):
    account_id = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    seller_account = models.ManyToManyField(Advertisement)

def __str__(self):
    return f"{self.first_name}"




    