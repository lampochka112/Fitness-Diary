# Fitness Diary 🏋️‍♂️

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Development-orange)](https://github.com/lampochka112/Fitness-Diary)

Веб-приложение для отслеживания тренировок и питания, созданное на Django. Позволяет пользователям вести дневник своих спортивных достижений, планировать рацион и анализировать прогресс.

## ✨ Основные возможности--------

*   **📊 Дневник тренировок:** Создание и запись деталей выполненных упражнений (подходы, повторения, вес).
*   **🍎 Учет питания:** Ведение дневника питания с подсчетом калорий и БЖУ (белков, жиров, углеводов).
*     **🎯 Планирование целей:** Постановка фитнес-целей (похудение, набор массы, поддержание формы) и отслеживание прогресса.
*     **📈 Визуализация прогресса:** Просмотр графиков и статистики по изменениям веса и силовых показателей.
*     **👤 Персональный профиль:** Настройка личных данных, целей и параметров тела.

## 🛠️ Технологический стек

*   **Backend:** [Django 4.2](https://www.djangoproject.com/) (Python)
*   **Frontend:** HTML, [Bootstrap 5](https://getbootstrap.com/), CSS
*   **База данных:** SQLite (для разработки), с возможностью перехода на PostgreSQL
*   **Аутентификация:** Django Allauth
*   **Графики:** Chart.js или аналогичная библиотека

## 🚀 Быстрый старт

Следуйте этим инструкциям, чтобы развернуть проект на вашей локальной машине для разработки и тестирования.

### Предварительные требования

Убедитесь, что на вашем компьютере установлены:
*   Python (версия 3.9 или выше)
*   pip (менеджер пакетов Python)
*   Git

### Установка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/lampochka112/Fitness-Diary.git
    cd Fitness-Diary
    ```

2.  **Создайте и активируйте виртуальное окружение (рекомендуется):**
    ```bash
    # Для Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Для Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Примените миграции базы данных:**
    ```bash
    python manage.py migrate
    ```

5.  **Создайте суперпользователя (для доступа к админ-панели):**
    ```bash
    python manage.py createsuperuser
    ```
    Следуйте инструкциям в терминале, чтобы задать логин, email и пароль.

6.  **Запустите сервер для разработки:**
    ```bash
    python manage.py runserver
    ```
    
7.  **Откройте браузер и перейдите по адресу:**
    *   Основное приложение: [http://127.0.0.1:8000](http://127.0.0.1:8000)
    *   Админ-панель: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


