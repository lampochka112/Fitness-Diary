from django.test import TestCase
from django.contrib.auth.models import User
from .models import FoodItem, Meal
from .forms import MealForm

class DiaryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.food = FoodItem.objects.create(
            name='Test Food',
            calories=100,
            protein=10,
            carbs=20,
            fat=5
        )

    def test_food_item_creation(self):
        self.assertEqual(self.food.name, 'Test Food')
        self.assertEqual(self.food.calories, 100)

    def test_meal_creation(self):
        meal = Meal.objects.create(
            user=self.user,
            food_item=self.food,
            quantity=2
        )
        self.assertEqual(meal.total_calories, 200)

    def test_meal_form_valid(self):
        form_data = {'food_item': self.food.id, 'quantity': 2}
        form = MealForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_food_search(self):
        response = self.client.get('/api/food-search/?q=apple')
        self.assertEqual(response.status_code, 200)