from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)






# Create your models here.
class Turtle(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    #this gives naming convention in the django admin
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'turtle_id': self.id})
    

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
      )
  
  turtle = models.ForeignKey(Turtle, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"