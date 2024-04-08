from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Turtle, Rock, Photo
from .forms import FeedingForm
import uuid # for random numbers (used in generating photo name)
import boto3 # aws sdk that lets us talk to our s3 bucket
import os # this lets us talk to the .env
# Define the home view

def some_function(request):
    secret_key = os.environ['SECRET_KEY']
    
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
 
def disassoc_rock(request, turtle_id, rock_id):
	turtle = Turtle.objects.get(id=turtle_id)
	turtle.rocks.remove(rock_id)
	return redirect('detail',turtle_id=turtle_id)
 
  
# turtles/<int:turtle_id>/assoc_rock/<int:rock_id>/
def assoc_rock(request, turtle_id, rock_id):
	print(turtle_id, rock_id )
	turle = Turtle.objects.get(id=turtle_id)
	turle.rocks.add(rock_id)# adding a row to our through table the one with 2 foriegn keys in sql
	return redirect('detail', turtle_id=turtle_id)  
  
  

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
  id_list = turtle.rocks.all().values_list('id')
  available_rocks = Rock.objects.exclude(id__in=id_list)
  return render(request, 'turtles/detail.html', {
    # include the turtle and feeding_form in the context
    'turtle': turtle, 'feeding_form': feeding_form,
    'available_rocks' : available_rocks, 
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
        # now we want to make sure we add the turtle id to the new_feeding
        new_feeding.turtle_id = turtle_id
        new_feeding.save() # this is adding a feeding row to the the feeding table in psql
    return redirect('detail', turtle_id=turtle_id) #turtle_id is the name of the param in the url path, turtle_id is the id o fthe turtle from the url request
  
class RockList(ListView):
    model = Rock


class RockDetail(DetailView):
    model = Rock


class RockCreate(CreateView):
    model = Rock
    fields = '__all__'


class RockUpdate(UpdateView):
    model = Rock
    fields = ['name', 'color']


class RockDelete(DeleteView):
    model = Rock
    success_url = '/rocks/'