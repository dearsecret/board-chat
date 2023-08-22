from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GENDER_CHOICES(models.TextChoices):
        MALE = ("남성", "male")
        FEMALE = ("여성", "female")

    gender = models.CharField(
        null=True, blank=True, max_length=120, choices=GENDER_CHOICES.choices
    )

    # username = models.CharField(unique=True, max_length=120)
    # phonenum = models.CharField(max_length=12, null=True, blank=True, default=True)
    # first_name = models.CharField(max_length=12, editable=False)
    # last_name = models.CharField(max_length=12, editable=False)
    # host = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Dong SOO! {self.username}"


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, related_name="profile", on_delete=models.CASCADE
    )
    avatar = models.URLField()
    bio = models.TextField(max_length=2000)
