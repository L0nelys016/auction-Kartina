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