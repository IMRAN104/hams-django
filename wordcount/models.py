from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Text(models.Model):
    text = models.CharField(max_length=1000, default="lorem ipsum....")
    no_of_words = models.IntegerField(default=0)

    def __str__(self):
        return "spouse name" + self.text + " No of Words: " + self.no_of_words
