from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-meal/', views.add_meal, name='add_meal'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/add/', views.add_workout, name='add_workout'),
    path('workouts/<int:pk>/edit/', views.edit_workout, name='edit_workout'),
    path('workouts/<int:pk>/delete/', views.delete_workout, name='delete_workout'),
    path('progress/', views.progress_photos, name='progress_photos'),
    path('api/food-search/', views.food_search_api, name='food_search_api'),
]