
# Register your models here.
from django.contrib import admin
# import your models here
from .models import Turtle, feeding, Rock

# Register your models here
admin.site.register(Turtle)
admin.site.register(feeding)
admin.site.register(Rock)

