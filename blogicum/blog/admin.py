"""(* Проект «Blogicum». Приложение «Blog». Администраторская часть *)"""

# /// Подключение моделей /// #
from blog.models import Category, Comment, Location, Post

# /// Администратор /// #
from django.contrib import admin

# /// Лимит списка /// #
from blogicum.settings import LIST_LIMIT


""" (* Раздел реализации *) """


""" { Классы } """


# // Класс «CategoryAdmin» // #
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "slug", "is_published")
    list_editable = ("description", "slug", "is_published")
    search_fields = ("title",)
    list_filter = ("is_published",)
    list_display_links = ("title",)
    list_per_page = LIST_LIMIT


# // Класс «LocationAdmin» // #
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    list_editable = ("is_published",)
    search_fields = ("name",)
    list_filter = ("is_published",)
    list_display_links = ("name",)
    list_per_page = LIST_LIMIT


# // Класс «CommentAdmin» // #
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = LIST_LIMIT


# // Класс «PostAdmin» // #
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "is_published",
        "pub_date",
        "category",
        "location",
    )
    list_editable = ("is_published", "pub_date", "category")
    search_fields = ("title",)
    list_filter = ("is_published",)
    list_display_links = ("title",)
    list_per_page = LIST_LIMIT
