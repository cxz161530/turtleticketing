
# Register your models here.
from django.contrib import admin
# import your models here
from .models import Turtle, Feeding, Rock

# Register your models here
admin.site.register(Turtle)
admin.site.register(Feeding)
admin.site.register(Rock)
