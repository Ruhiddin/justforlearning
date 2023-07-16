from django.shortcuts import render

tasks = ['foo', 'bar', 'bazz']
# Create your views here.
def index(request):
    return render(request, 'todolist/index.html', {'tasks': tasks})