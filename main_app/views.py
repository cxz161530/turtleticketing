from django.shortcuts import render, redirect

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

def add_feeding(request, turtle_id):
    # process the form requets from the client
    form = FeedingForm(request.POST)
    #request>POST is like req.body, its the contents of the form
    #validate the form
    if form.is_valid():
        #create an in memory instance (on django) or our data
        #to be added to psql, commit=False, dont save to db yet
        new_feeding =form.save(commit=False)
        # now we want to make sure we add the cat id to the new_feeding
        new_feeding.turtle_id = turtle_id
        new_feeding.save() # this is adding a feeding row to the the feeding table in psql
    return redirect('detail', turtle_id=turtle_id) #turtle_id is the name of the param in the url path, turtle_id is the id o fthe turtle from the url request