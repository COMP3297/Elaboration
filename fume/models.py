from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Game(models.Model):
    game = models.CharField(max_length=200,blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    game_id = models.CharField(max_length=200,blank=True, null=True)
    gameDescription = models.TextField(blank=True)
    def __str__(self):
        return self.game


class Tag(models.Model):
    tag = models.CharField(max_length=50,blank=True, null=True)
    creator = models.CharField(max_length=200,blank=True, null=True)
    game = models.ForeignKey(Game,blank=True, null=True)
    def __str__(self):
        return self.tag

    
class Tagging(models.Model):
    #userId = models.ForeignKey(User)
    tag = models.ForeignKey(Tag,blank=True, null=True)
    def __str__(self):
        return self.tag
    
class Purchase(models.Model):
    userId = models.ForeignKey(User,blank=True, null=True)
    game = models.ForeignKey(Game,blank=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User)
    game = models.ManyToManyField(Game,blank=True, null=True)
    def addGame(self,game):
        self.game.add(game)
    def getTotal(self):
        games = self.game.all()
        amount = self.game.all().count()
        totalAmount = 0
        for gme in games:
            price = Game.objects.get(game=gme).price
            totalAmount = totalAmount + price
        return totalAmount

class Reward(models.Model):
    timeReceived = models.DateTimeField(blank=True, null=True)
    amount = models.CharField(max_length=200)
    def receiveReward(self):                    # to record the time when the reward is received
            self.timeReceived = timezone.now()
            self.save()
            
class Administrator(models.Model):
    adminID = models.CharField(max_length=200)

class Recommendation(models.Model):
	userId = models.ForeignKey(User)
	def __str__(self):
		return self.userId
