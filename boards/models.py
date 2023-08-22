from django.db import models
from common.models import CommonModel

# Create your models here.


class Board(CommonModel):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    writer = models.ForeignKey(
        "users.User",
        related_name="boards",
        on_delete=models.CASCADE,
    )
    hits = models.PositiveIntegerField(default=0)

    liked_user = models.ManyToManyField(
        "users.User",
        through="Preference",
        related_name="preferences",
        default=None,
    )
    comment_user = models.ManyToManyField(
        "users.User",
        through="Comment",
        related_name="comments",
        default=None,
    )

    def count(self):
        return f"{self.comment_user.count()}"

    @property
    def comments_count(self):
        pass

    class Meta:
        verbose_name_plural = "게시글"


class Comment(CommonModel):
    board = models.ForeignKey(
        "boards.Board",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    content = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "댓글"


class Preference(CommonModel):

    """평가에 이용되는 모델"""

    class PreferChoices(models.IntegerChoices):
        LIKE = 1, "like"
        DISLIKE = -1, "dislike"

    prefer = models.IntegerField(choices=PreferChoices.choices)
    board = models.ForeignKey(
        "boards.Board",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name_plural = "좋아요"


class Favorite(CommonModel):
    user = models.ForeignKey(
        "users.User", related_name="favorites", on_delete=models.CASCADE
    )
    board = models.ManyToManyField("boards.Board", related_name="favorites")

    class Meta:
        verbose_name_plural = "즐겨찾기"


class PostImage(CommonModel):
    post = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
    url = models.URLField()
