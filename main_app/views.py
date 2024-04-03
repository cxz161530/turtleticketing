from django.shortcuts import render

turtles = [
  {'name': 'Franklin', 'breed': 'box turtle', 'description': 'will do anything for grapes', 'age': 13},
  {'name': 'Sheldon', 'breed': 'russian tortise', 'description': 'slow and steady', 'age': 82},
      {'name': 'Bugs', 'breed': 'red ear slidder', 'description': 'faster than a hair', 'age': 22},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def turtles_index(request):
    return render(request, 'turtles/index.html', {
        'turtles': turtles
    })
