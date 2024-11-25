from django.urls import path
from . import views 


urlpatterns = [
    path("all_todo's/", views.AllTodos.as_view()),
    path("all_todo's/<int:id>/", views.TodoDetail.as_view()),
]