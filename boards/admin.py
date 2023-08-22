from django.contrib import admin
from .models import Board, Comment, Favorite, Preference

# Register your models here.


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_count_comment",
        "get_like",
    )

    def get_count_comment(self, obj):
        return f"{obj.comment_user.count()}"

    def get_like(self, obj):
        return f"{obj.count()}"

    get_like.short_description = "좋아요"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    pass
