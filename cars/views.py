from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    text = "car page"
    context = {'text': text}
    return render(request, 'cars.html', context)