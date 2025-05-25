"""(* Проект «Blogicum». Приложение «Blog». Вспомогательный класс *)"""

# /// Необходимость логина /// #
from django.contrib.auth.mixins import LoginRequiredMixin

# /// Страницы (ошибки или данные) /// #
from django.shortcuts import get_object_or_404, redirect

# /// Reverse /// #
from django.urls import reverse

# /// Зона времени /// #
from django.utils import timezone

# /// Модели /// #
from .models import Comment, Post


""" (* Раздел реализации *) """


""" { Классы } """


# // Класс «CommentMixin» // #
class CommentMixin(LoginRequiredMixin):
    model = Comment
    template_name = "blog/comment.html"
    pk_url_kwarg = "comment_pk"

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect("blog:post_detail", pk=self.kwargs.get("pk"))

        get_object_or_404(
            Post,
            pk=self.kwargs.get("pk"),
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse(
            "blog:post_detail", kwargs={"pk": self.kwargs.get("pk")}
        )


# // Класс «UserIsAuthorMixin» // #
class UserIsAuthorMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect("blog:post_detail", pk=kwargs.get("pk"))

        return super().dispatch(request, *args, **kwargs)
