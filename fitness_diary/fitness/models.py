from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Пол')
    height = models.PositiveIntegerField(null=True, blank=True, verbose_name='Рост (см)')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Вес (кг)')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Фото профиля')
    
    def __str__(self):
        return self.username