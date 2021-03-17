from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('deletetodo', views.deletetodo, name='deletetodo'),
    path('edittodo', views.edittodo, name='edittodo')
]