from django import forms
from .models import *
from wtforms.validators import Length, DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6)])

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

class EditWorkoutForm(FlaskForm):
    date = DateField('Дата тренировки', validators=[DataRequired()])
    workout_type = StringField('Тип тренировки', validators=[DataRequired()])
    duration = IntegerField('Длительность (мин)', validators=[DataRequired()])
    exercises = TextAreaField('Упражнения и подходы', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')
        
class EditNutritionForm(FlaskForm):
    date = DateField('Дата', validators=[DataRequired()])
    meal = StringField('Прием пищи/Блюдо', validators=[DataRequired()])
    calories = IntegerField('Калории', validators=[DataRequired()])
    protein = IntegerField('Белки (г)', validators=[DataRequired()])
    fat = IntegerField('Жиры (г)', validators=[DataRequired()])
    carbs = IntegerField('Углеводы (г)', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')