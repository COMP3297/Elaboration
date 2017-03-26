from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from fume.models import Game


def featured(request):
    return render(request, 'fume/featured.html', {})

def games(request, game_id):
    #game = Game.objects.get(id=game_id)
    return render(request, 'fume/'+ game_id + '.html')
    
def purchase(request):
    return render(request, 'fume/purchase.html', {})


