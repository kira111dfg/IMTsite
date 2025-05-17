
from django import forms

from .models import IMT,Dish,Dietary

class CountForm(forms.Form):
    weight = forms.IntegerField(min_value=30, max_value=300)
    height = forms.IntegerField(min_value=100, max_value=200)
    

class PostForm(forms.ModelForm):
    class Meta:
        model=Dish
        exclude=['author']

class DietForm(forms.ModelForm):
    class Meta:
        model=Dietary
        exclude=['author']