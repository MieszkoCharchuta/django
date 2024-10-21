from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    # Przeciążenie klasy string, czyli co ma być wyświetlone zamiast klasy tego obiektu (Post)
    # To po prostu cecha programowania obiektowego w pythonie
    def __str__(self):
        return self.title