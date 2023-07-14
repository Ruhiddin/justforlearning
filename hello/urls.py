from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:firstname>&<str:lastname>', views.greet, name='greet'),
    ]