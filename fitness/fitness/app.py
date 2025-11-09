from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user
from fitness_diary import create_app, db
from models import Workout, Nutrition
from forms import EditWorkoutForm, EditNutritionForm
from datetime import datetime

app = create_app()

@app.route('/edit_workout/<int:workout_id>', methods=['GET', 'POST'])
@login_required
def edit_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    
    if workout.user_id != current_user.id:
        abort(403)
    
    form = EditWorkoutForm()
    
    if form.validate_on_submit():
        workout.date = form.date.data
        workout.workout_type = form.workout_type.data
        workout.duration = form.duration.data
        workout.exercises = form.exercises.data
        
        db.session.commit()
        flash('Тренировка успешно обновлена!', 'success')
        return redirect(url_for('diary'))
    
    elif request.method == 'GET':
        form.date.data = workout.date
        form.workout_type.data = workout.workout_type
        form.duration.data = workout.duration
        form.exercises.data = workout.exercises
    
    return render_template('edit_workout.html', form=form, workout=workout)

@app.route('/edit_nutrition/<int:nutrition_id>', methods=['GET', 'POST'])
@login_required
def edit_nutrition(nutrition_id):
    nutrition = Nutrition.query.get_or_404(nutrition_id)
    
    if nutrition.user_id != current_user.id:
        abort(403)
    
    form = EditNutritionForm()
    
    if form.validate_on_submit():
        nutrition.date = form.date.data
        nutrition.meal = form.meal.data
        nutrition.calories = form.calories.data
        nutrition.protein = form.protein.data
        nutrition.fat = form.fat.data
        nutrition.carbs = form.carbs.data
        
        db.session.commit()
        flash('Запись о питании успешно обновлена!', 'success')
        return redirect(url_for('diary'))
    
    elif request.method == 'GET':
        form.date.data = nutrition.date
        form.meal.data = nutrition.meal
        form.calories.data = nutrition.calories
        form.protein.data = nutrition.protein
        form.fat.data = nutrition.fat
        form.carbs.data = nutrition.carbs
    
    return render_template('edit_nutrition.html', form=form, nutrition=nutrition)

if __name__ == '__main__':
    app.run(debug=True)