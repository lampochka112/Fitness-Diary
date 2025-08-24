# Fitness Diary - Дневник питания и тренировок

## Установка и запуск

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте: `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Примените миграции: `python manage.py migrate`
6. Создайте суперпользователя: `python manage.py createsuperuser`
7. Запустите сервер: `python manage.py runserver`

## API endpoints

- `GET /api/food-search/?q=apple` - поиск еды через Nutritionix API
- `GET /api/workouts/` - список тренировок
- `POST /api/meals/` - добавление приема пищи

## Основные функции

- 📊 Отслеживание питания и калорий
- 💪 Учет тренировок
- 📸 Фото прогресса
- 📰 Новостная лента
- 👥 Социальные функции
- 🔔 Напоминания по email