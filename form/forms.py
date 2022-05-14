from importlib.metadata import files
from typing import OrderedDict
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
