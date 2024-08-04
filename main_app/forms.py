# forms.py

from django.forms import ModelForm
from .models import feeding

class feedingForm(ModelForm):
  class Meta:
    model = feeding
    fields = ['date', 'meal']
