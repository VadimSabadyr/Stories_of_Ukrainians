from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Author(AbstractUser):
    pseudonym = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Publication(models.Model):
    title = models.CharField(max_length=255)
    story = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="cars")

    def __str__(self):
        return self.title
