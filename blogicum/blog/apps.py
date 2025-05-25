"""(* Проект «Blogicum». Приложение «Blog». Приложения *)"""

# /// Конфигуратор приложений /// #
from django.apps import AppConfig


""" (* Раздел реализации *) """


""" { Классы } """


# // Класс «BlogConfig» // #
class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = "Блог"
