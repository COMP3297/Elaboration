from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
    game = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name    


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    creater = models.CharField(max_length=200)
    def __str__(self):
        return self.tag

    
class Tagging(models.Model):
    #userId = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    def __str__(self):
        return self.tag
    
class Purchase(models.Model):
    userId = models.ForeignKey(User)
    game = models.ForeignKey(Game)

class Cart(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)

class Reward(models.Model):
    timeReceived = models.DateTimeField(blank=True, null=True)
    amount = models.
    def receiveReward(self):
            self.timeReceived = timezone.now()
            self.save()
class Administrator(models.Model):
    ID = models.CharField(max_length=200)

