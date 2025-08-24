from django import forms
from .models import *

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['food_item', 'quantity']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['food_item'].queryset = FoodItem.objects.all()

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'duration', 'calories_burned', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class ProgressPhotoForm(forms.ModelForm):
    class Meta:
        model = ProgressPhoto
        fields = ['photo', 'notes']