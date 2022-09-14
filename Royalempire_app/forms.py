from django import forms
from django.forms import ModelForm
from .models import *


red = "red"
blue = "blue"
yellow = "yellow"
green = "green"
black = "black"
white = "white"
colours = [(green,"green"), (yellow,"yellow"), (blue,"blue"), (red,"red"), (black,"black"), (white,"white")]

class available_items_form(ModelForm):
    item_img = forms.ImageField()
    class Meta:
        model = available_items
        fields = (
            'item_name',
            'item_color',
            'item_img',
        )

class chartForm(ModelForm):
    item_color = forms.ChoiceField(choices="colours", )
    class meta:
        model = chart
        fields = (
            "item_name",
            "item_color",
            "quantity",
            "price",
            "item_image",   
        )
