"""(* Проект «Blogicum». Приложение «Blogicum». Главный файл настроек *)"""

# /// Операционная система /// #
import os

# /// Операционная система /// #
from django.core.asgi import get_asgi_application


""" (* Раздел реализации *) """


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
application = get_asgi_application()
