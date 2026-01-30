from django.db import models
# from django.core import validators as v
# from django.core.exceptions import ValidationError
# from .validators import validate_move_name


class UserProfiles(models.Model):
    # We could use the same validator we created for the Pokemon Name for our Moves Name
    account_id = models.IntegerField(unique = True, default = 1)
    street_name = models.CharField(max_length=250)
    street_number = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    city = models.CharField(max_length=250)


    
    # # We want each move to have PP between 0 if they've utilized this move too much and 30 depending on it's max capability
    # pp = models.IntegerField(default=20, validators=[
    #                          v.MinValueValidator(1)])
    # # We want to know just how much Power each move has
    # power = models.PositiveIntegerField(
    #     default=80, validators=[v.MaxValueValidator(120)])

    # def __str__(self):
    #     return f"| {self.name} | accuracy: {self.accuracy} | power: {self.power} | current_pp: {self.pp}/{self.maxPP} |"

    # def increase_max_pp(self, increment):
    #     self.maxPP = self.maxPP + increment
    #     self.save()
from django.db import models

# Create your models here.
