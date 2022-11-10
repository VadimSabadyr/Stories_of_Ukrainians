from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return {self.name}


class Author(AbstractUser):
    license_number = models.TextChoices("brilliant", "good")

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

