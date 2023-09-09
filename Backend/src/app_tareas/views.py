# En app_tareas/views.py
from django.shortcuts import render

def vista_react(request):
    return render(request, 'react_template.html')
  # Verifica la ruta de acceso a la plantilla

