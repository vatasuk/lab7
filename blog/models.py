from  django.contrib.auth.models import  User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE);
    def __str__(self):
        return self.title