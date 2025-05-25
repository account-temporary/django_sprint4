"""(* Проект «Blogicum». Приложение «Pages». Запросы URL *)"""

# /// Работа с директориями /// #
from django.urls import path

# /// View-функции /// #
from . import views


""" { Константы } """


# /// Имя приложения /// #
app_name = "pages"
# /// Запросы /// #
urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("rules/", views.RulesView.as_view(), name="rules"),
]
