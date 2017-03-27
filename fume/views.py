from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from fume.models import Game, Cart


def featured(request):
    return render(request, 'fume/featured.html', {})

def games(request, game_id):
    #game = Game.objects.get(id=game_id)
    addCart = Game.objects.filter(id=game_id)
    return render(request, 'fume/'+ game_id + '.html')
    
def purchase(request, game_id):
    addCart=Game.objects.filter(id=game_id)
    addedCart=Cart(game=addCart[0])
    addedCart.save()
    games = Cart.objects.all()
    amount = Cart.objects.all().count()
    totalAmount = 0
    for gme in games:
        totalAmount = totalAmount + gme.game.price
    return render(request, 'fume/purchase.html', {'games': games, 'amount': amount, 'totalAmount': totalAmount})

def purchaseAll(request):
    Cart.objects.all().delete()
    return render(request, 'fume/featured.html', {})


