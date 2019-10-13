from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(null=True, max_length=255)
    pub_date = models.DateTimeField(
        null=True, auto_now=False, auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(null=True, upload_to='images')
