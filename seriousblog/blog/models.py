from django.db import models


class Post(models.Model):
    tittle = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.tittle
