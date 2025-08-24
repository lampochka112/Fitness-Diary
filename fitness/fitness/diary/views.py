from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
from .forms import *
import requests
import json
import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    # Логируем посещение dashboard
    logger.info(f"User {request.user.username} accessed dashboard")
    
    today = timezone.now().date()
    meals = Meal.objects.filter(user=request.user, date__date=today)
    workouts = Workout.objects.filter(user=request.user, date__date=today)
    
    total_calories = sum(meal.food_item.calories * meal.quantity for meal in meals)
    total_protein = sum(meal.food_item.protein * meal.quantity for meal in meals)
    
    return render(request, 'diary/dashboard.html', {
        'meals': meals,
        'workouts': workouts,
        'total_calories': total_calories,
        'total_protein': total_protein
    })

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, user=request.user)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, 'Прием пищи добавлен!')
            return redirect('dashboard')
    else:
        form = MealForm(user=request.user)
    
    return render(request, 'diary/add_meal.html', {'form': form})

@login_required
def food_search_api(request):
    query = request.GET.get('q', '')
    if query:
        # Интеграция с Nutritionix API
        headers = {
            'x-app-id': settings.NUTRITIONIX_APP_ID,
            'x-app-key': settings.NUTRITIONIX_APP_KEY,
            'Content-Type': 'application/json'
        }
        data = {'query': query}
        response = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', 
                               headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            return JsonResponse(response.json())
    
    return JsonResponse({'foods': []})