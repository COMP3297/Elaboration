from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
    game = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.game


class User(models.Model):
    name = models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name    


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag

    
class Tagging(models.Model):
    userId = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    def __str__(self):
        return self.userId

    
class Purchase(models.Model):
    userId = models.ForeignKey(User)
    game = models.ForeignKey(Game)



    