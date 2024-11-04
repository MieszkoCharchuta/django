from django.db import models
from select import select


# Create your models here.

# We have a relation many-to-one (one Category has many posts, one posts has only one category)
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) #Cascade means that deleting a category deletes all posts in it
    title = models.CharField(max_length=140)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=True)

    # Przeciążenie klasy string, czyli co ma być wyświetlone zamiast klasy tego obiektu (Post)
    # To po prostu cecha programowania obiektowego w pythonie
    def __str__(self):
        return self.title