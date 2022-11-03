from django.http import HttpResponse
from django.shortcuts import render

from keloksiBuku import views as viewsApps


def index(request):
    return render(request, 'index.html')
