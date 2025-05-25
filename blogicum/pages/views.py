"""(* Проект «Blogicum». Приложение «Pages». Запросы URL *)"""

# /// Пользователь /// #
from django.contrib.auth.forms import UserCreationForm

# /// Пользователь /// #
from django.shortcuts import render

# /// Пользователь /// #
from django.urls import reverse_lazy

# /// Пользователь /// #
from django.views.generic import CreateView, TemplateView


""" (* Раздел реализации *) """


""" { Классы } """


# /// Класс «AboutView» /// #
class AboutView(TemplateView):
    template_name = "pages/about.html"


# /// Класс «RulesView» /// #
class RulesView(TemplateView):
    template_name = "pages/rules.html"


# /// Класс «RegistationCreateView» /// #
class RegistationCreateView(CreateView):
    template_name = "registration/registration_form.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy(
            "blog:profile",
            kwargs={"username": self.request.POST.get("username")},
        )


""" { Функции } """


# /// Функция «page_not_found» /// #
def page_not_found(request, exception):
    return render(request, "pages/404.html", status=404)


# /// Функция «server_error» /// #
def server_error(request):
    return render(request, "pages/500.html", status=500)


# /// Функция «csrf_failure» /// #
def csrf_failure(request, reason=""):
    return render(request, "pages/403csrf.html", status=403)
