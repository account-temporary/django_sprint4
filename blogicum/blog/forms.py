"""(* Проект «Blogicum». Приложение «Blog». Формы *)"""

# /// Подключение моделей /// #
from blog.models import Comment, Post, User

# /// Формы /// #
from django import forms

# /// Зона времени /// #
from django.utils import timezone


""" (* Раздел реализации *) """


""" { Классы } """


# // Класс «PostForm» // #
class PostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        initial=timezone.now(),
        label="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — "
            "можно делать отложенные публикации."
        ),
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Post
        exclude = ("author", "is_published")
        widgets = {
            "text": forms.Textarea(attrs={"rows": "5"}),
        }


# // Класс «CommentForm» // #
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"rows": "4"}),
        }


# // Класс «UserForm» // #
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
