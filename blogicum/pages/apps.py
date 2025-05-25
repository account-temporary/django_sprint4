"""(* Проект «Blogicum». Приложение «Pages». Приложения *)"""

# /// Конфигуратор настроек /// #
from django.apps import AppConfig


""" { Классы } """


# /// Класс «PagesConfig» /// #
class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
