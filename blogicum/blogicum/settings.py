"""(* Проект «Blogicum». Приложение «Blogicum». Главный файл настроек *)"""

# /// Работа с директориями /// #
from pathlib import Path


""" { Константы } """


# /// Основная директория /// #
BASE_DIR = Path(__file__).resolve().parent.parent
# /// Секретный ключ /// #
SECRET_KEY = (
    "django-insecure-v9d*m0g_*p%wa!pcr)qdy#bwpp#)tt5v2!_0s4l*8luj&cblbv"
)
# /// Отладка /// #
DEBUG = True
# /// Хосты /// #
ALLOWED_HOSTS = ["127.0.0.1"]
# /// IPS /// #
INTERNAL_IPS = ["127.0.0.1"]
# /// Ссылка на перенаправление /// #
LOGIN_REDIRECT_URL = "blog:index"
# /// Логин /// #
LOGIN_URL = "login"
# /// Ссылка на страницу ошибки /// #
CSRF_FAILURE_VIEW = "pages.views.csrf_failure"
# /// Установленные приложения /// #
INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "pages.apps.PagesConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
]
# /// Межплатформенные функции /// #
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# /// ROOT_URLCONF /// #
ROOT_URLCONF = "blogicum.urls"
# /// Папка с шаблонами /// #
TEMPLATES_DIR = BASE_DIR / "templates"
# /// MEDIA_ROOT /// #
MEDIA_ROOT = BASE_DIR / "media"
# /// EMAIL_BACKEND /// #
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# /// EMAIL_FILE_PATH /// #
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
# /// TEMPLATES /// #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
# /// WSGI_APPLICATION /// #
WSGI_APPLICATION = "blogicum.wsgi.application"
# /// DATABASES /// #
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# /// AUTH_PASSWORD_VALIDATORS /// #
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]
# /// LANGUAGE_CODE /// #
LANGUAGE_CODE = "ru-RU"
# /// TIME_ZONE /// #
TIME_ZONE = "Europe/Moscow"
# /// USE_I18N /// #
USE_I18N = True
# /// USE_L10N /// #
USE_L10N = False
# /// USE_TZ /// #
USE_TZ = True
# /// STATIC_URL /// #
STATIC_URL = "/static/"
# /// STATICFILES_DIRS /// #
STATICFILES_DIRS = [BASE_DIR / "static"]
# /// DEFAULT_AUTO_FIELD /// #
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# /// POST_LIMIT /// #
POST_LIMIT = 10
# /// LIST_LIMIT /// #
LIST_LIMIT = 20
# /// CHARS_LIMIT /// #
CHARS_LIMIT = 20
