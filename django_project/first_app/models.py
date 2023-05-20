from django.db import models
import uuid

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(50, null=False)
    rating = models.FloatField(default=3)
    authors = models.ManyToManyField(Author, "books")

    def __repr__(self):
        return f"{self.title} ({self.rating})"