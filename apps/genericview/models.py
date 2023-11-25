from django.db import models


# Create your models here.
class AuthorGeneric(models.Model):
    first_name = models.CharField(max_length=202)
    last_name = models.CharField(max_length=202)
    age = models.IntegerField()
    job = models.CharField(max_length=202)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CategoryGeneric(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class BookGeneric(models.Model):
    title = models.CharField(max_length=202)
    author = models.ForeignKey(AuthorGeneric, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey(CategoryGeneric, on_delete=models.CASCADE, related_name='category')
    language = models.CharField(max_length=20)
    number_of_books = models.IntegerField()

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
