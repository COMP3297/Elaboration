from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from fume.models import Game, Cart
from fume.forms import NameForm


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

def tagedit(request, game_id):
    tag_id=game_id
    return render(request, 'fume/tag.html', {'tag_id':game_id})
    

def addtag(request):
    def get_name(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/featured')
    
        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

    return render(request, 'name.html', {'form': form})
    