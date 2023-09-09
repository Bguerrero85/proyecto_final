from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    dni = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True)
    nacionalidad = models.CharField(max_length=30, blank=True)

    # Agrega el argumento related_name a las relaciones
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        related_name='usuarios'  # Cambia 'usuarios' a lo que prefieras
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='usuarios'  # Cambia 'usuarios' a lo que prefieras
    )

    def __str__(self):
        return self.username
