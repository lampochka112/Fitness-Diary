from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'diary/index.html')

@login_required
def workout_list(request):
    return render(request, 'diary/workout_list.html')

@login_required
def workout_create(request):
    return render(request, 'diary/workout_form.html')

@login_required
def meal_list(request):
    return render(request, 'diary/meal_list.html')

@login_required
def meal_create(request):
    return render(request, 'diary/meal_form.html')

@login_required
def weight_tracking(request):
    return render(request, 'diary/weight_tracking.html')