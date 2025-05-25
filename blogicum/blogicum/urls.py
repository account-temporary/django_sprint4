"""(* Проект «Blogicum». Приложение «Blogicum». Запросы URL *)"""

# /// Работа с директориями /// #
from django.conf import settings

# /// Работа с директориями /// #
from django.conf.urls.static import static

# /// Работа с директориями /// #
from django.contrib import admin

# /// Работа с директориями /// #
from django.urls import include, path

# /// Работа с директориями /// #
from pages import views


""" { Константы } """


# /// Запросы /// #
urlpatterns = [
    path("", include("blog.urls", namespace="blog")),
    path("pages/", include("pages.urls", namespace="pages")),
    path("admin/", admin.site.urls),
    path(
        "auth/registration/",
        views.RegistationCreateView.as_view(),
        name="registration",
    ),
    path("auth/", include("django.contrib.auth.urls")),
]
urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
# /// Обработчик ошибок 404 /// #
handler404 = "pages.views.page_not_found"
# /// Обработчик ошибок 500 /// #
handler500 = "pages.views.server_error"
