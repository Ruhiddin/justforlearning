from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def greet(request, firstname, lastname):
    return render(request, 'hello/greet.html', {'firstname': firstname.capitalize(), 'lastname': lastname.capitalize()})