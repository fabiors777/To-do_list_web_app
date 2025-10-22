from django.contrib import admin
from django.urls import path

# from manage_todos.views import todo_list - Alterado para usar classe
from manage_todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)  # Incluido para usar com a classe

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),  # para usar no modo class
    # path("", todo_list), Mode de usar com a função
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>/", TodoCompleteView.as_view(), name="todo_complete"),
]
