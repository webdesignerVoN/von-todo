from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add', views.addTodo, name="add"),
    path('done/<todo_id>', views.doneTodo, name="done"),
    path('deletedone', views.deleteDone, name="deletedone"),
    path('deleteall', views.deleteAll, name="deleteall"),
]
