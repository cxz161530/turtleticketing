from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Turtle
from .forms import FeedingForm

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class TurtleCreate(CreateView):
    model = Turtle
    fields = '__all__'

class TurtleUpdate(UpdateView):
  model = Turtle
  # Let's disallow the renaming of a turtle by excluding the name field!
  fields = ['breed', 'description', 'age']

class TurtleDelete(DeleteView):
  model = Turtle
  success_url = '/turtles'
    
    

def turtles_index(request):
    turtles = Turtle.objects.all()
    return render(request, 'turtles/index.html', {
        'turtles': turtles
    })
def turtles_detail(request, turtle_id):
  turtle = Turtle.objects.get(id=turtle_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'turtles/detail.html', {
    # include the cat and feeding_form in the context
    'turtle': turtle, 'feeding_form': feeding_form
  })