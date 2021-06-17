from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["title", "category", "author","created_at", "id"]
    inlines = [RecipeInline]


@admin.register(Category)
class AdminCategory(MPTTModelAdmin):
    pass


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass