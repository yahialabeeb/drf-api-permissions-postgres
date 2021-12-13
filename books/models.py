from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.
class Book(models.Model):
    x = [
        ("novel","novel"),
        ("religious","religious"),
        ("political","political"),
        ("social","social")
    ]
    title = models.CharField(max_length = 128)
    author = models.CharField(max_length = 128)
    description = models.TextField()
    category = models.CharField(max_length = 64, choices = x ,default = x[0][0])
    addby = models.ForeignKey(get_user_model(), on_delete=CASCADE, null=True )
    def __str__(self):
        return str(self.title)