"""(* Проект «Blogicum». Приложение «Blog». Администраторская часть *)"""

""" (* Раздел объявлений *) """


""" { Подключение вспомогательных модулей } """


# /// Модель пользователя /// #
from django.contrib.auth import get_user_model  # noqa: E402

# /// Модель пользователя /// #
from django.db import models  # noqa: E402

# /// Модель пользователя /// #
from django.urls import reverse  # noqa: E402

# /// Модель пользователя /// #
from blogicum.settings import CHARS_LIMIT  # noqa: E402


""" { Переменные } """


# /// Пользователь /// #
User = get_user_model()


""" (* Раздел реализации *) """


""" { Классы } """


# // Класс «DefaultVerboseNameMadel» // #
class DefaultVerboseNameMadel(models.Model):
    class Meta:
        abstract = True
        default_related_name = "%(class)ss"


# // Класс «PublishedModel» // #
class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Добавлено"
    )

    class Meta:
        abstract = True


# // Класс «TitleModel» // #
class TitleModel(PublishedModel):
    title = models.CharField(verbose_name="Заголовок", max_length=256)

    class Meta:
        abstract = True


# // Класс «Location» // #
class Location(PublishedModel):
    name = models.CharField(verbose_name="Название места", max_length=256)

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


# // Класс «Category» // #
class Category(TitleModel):
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        "Идентификатор",
        unique=True,
        help_text=(
            "Идентификатор страницы для URL; "
            "разрешены символы латиницы, цифры, "
            "дефис и подчёркивание."
        ),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


# // Класс «Post» // #
class Post(TitleModel):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — "
            "можно делать отложенные публикации."
        ),
    )
    image = models.ImageField(
        verbose_name="Фото", upload_to="posts_images", blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )

    class Meta(DefaultVerboseNameMadel.Meta):
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})


# // Класс «Comment» // #
class Comment(models.Model):
    text = models.TextField(verbose_name="Коментрий")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Добавлено"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор комментария"
    )

    class Meta(DefaultVerboseNameMadel.Meta):
        verbose_name = "коментрий"
        verbose_name_plural = "Коментрии"
        ordering = ("created_at",)

    def __str__(self):
        return (
            f'Коментарий "{self.author}" к посту "{self.post}": '
            f'"{self.text[:CHARS_LIMIT]}"'
        )
