from django.shortcuts import render
from .models import Fuente
from django.utils.translation import gettext as _

# Create your views here.

def home(request):
    fuentes = Fuente.objects.all()
    return render(request, "salida.html", {"fuentes": fuentes})