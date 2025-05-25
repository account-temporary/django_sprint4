"""(* Проект «Blogicum». Приложение «Blogicum». Запросы URL *)"""

# /// Операционная система /// #
import os

# /// get_wsgi_application /// #
from django.core.wsgi import get_wsgi_application


""" (* Раздел реализации *) """


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogicum.settings")
application = get_wsgi_application()
