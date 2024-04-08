from django.db import models
from django.urls import reverse
from datetime import date

class Rock(models.Model):
	size = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	
	def __str__(self):
		return self.size

	def get_absolute_url(self):
		return reverse('rocks_detail', kwargs={'pk': self.id})
   


# Create your models here.
class Turtle(models.Model):
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
	rocks = models.ManyToManyField(Rock)
	#this gives naming convention in the django admin
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('detail', kwargs={'turtle_id': self.id})
	def fed_for_today(self):
		return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    turtle = models.ForeignKey(Turtle, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for turtle_id: {self.turtle_id} @{self.url}"
    
	# A tuple of 2-tuples
MEALS = (
	('B', 'Breakfast'),
	('L', 'Lunch'),
	('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField("feeding date")
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0],
    )

    # create a turtle_id Foreign Key in psql
    # we don't put the id, django does automatically
    turtle = models.ForeignKey(Turtle, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
	












# class Feeding(models.Model):
# # the first optional positional argument overrides the label
#   date = models.DateField('feeding date')
#   meal = models.CharField(
# 	  max_length=1,
# 	  choices=MEALS,
# 	  default=MEALS[0][0]
# 	  )
  
#   	turtle = models.ForeignKey(Turtle, on_delete=models.CASCADE)
 
# 	def __str__(self):
# 	# Nice method for obtaining the friendly value of a Field.choice
#  	return f"{self.get_meal_display()} on {self.date}"
#   # change the default sort
#   	# class Meta:
# 	# 	ordering = ['-date']