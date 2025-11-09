from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/create/', views.workout_create, name='workout_create'),
    path('meals/', views.meal_list, name='meal_list'),
    path('meals/create/', views.meal_create, name='meal_create'),
    path('weight/', views.weight_tracking, name='weight_tracking'),
]