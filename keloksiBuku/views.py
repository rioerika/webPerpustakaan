from django.shortcuts import render

# Create your views here.


def koleksi(request):
    return render(request, 'koleksi.html')
