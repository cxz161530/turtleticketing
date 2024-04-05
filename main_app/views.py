from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Turtle

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class TurtleCreate(CreateView):
    model = Turtle
    fields = '__all__'

def turtles_index(request):
    turtles = Turtle.objects.all()
    return render(request, 'turtles/index.html', {
        'turtles': turtles
    })
def turtles_detail(request, turtle_id):
	# tell the model to find the row that matches cat_id from the request in the database
	turtle = Turtle.objects.get(id=turtle_id)
	return render(request, 'turtles/detail.html', {
		'turtle': turtle
		# turtle (the key) is the variable name in turtles/detail.html 
	})