from django.contrib.auth.models import AbstractUser
from django.db import models

class modern_picture(models.Model):
    title = models.CharField('Название картины', max_length=50)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class classic_picture(models.Model):
    title = models.CharField('Название картины', max_length=50)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class abstract_picture(models.Model):
    title = models.CharField('Название картины', max_length=50)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class portret_picture(models.Model):
    title = models.CharField('Название картины', max_length=50)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='')

    def __str__(self):
        return self.title


class favorites_picture(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='favorites/')
    original_id = models.IntegerField()  # ID оригинальной картины
    picture_type = models.CharField(max_length=10)  # 'modern', 'classic' и т.д.

    class Meta:
        unique_together = ('original_id', 'picture_type')


