from django.db import models
from apps.authentication.models import User

# Create your models here.
class FoodLog(models.Model):
    date = models.DateField(auto_now_add=True)
    name_of_food = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=9, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'),])
    meal = models.CharField(max_length=100, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'),])
    description = models.TextField(blank=True)
    calories = models.IntegerField()
    updated_at = models.DateField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name_of_food + "-" + self.meal
