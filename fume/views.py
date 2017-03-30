from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from fume.models import Game,Cart,Tag
from fume.forms import NameForm


def featured(request):
	return render(request, 'fume/featured.html', {})

def games(request, game_id):
	#game = Game.objects.get(id=game_id)
	print(game_id)
	addCart = Game.objects.filter(id=game_id)
	return render(request, 'fume/'+ game_id + '.html', {'tag_id':game_id})
	
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
	print(game_id)
	
	return render(request, 'fume/tag.html', {'tag_id':game_id})
	

def addtag(request, game_id):
	print (1111)
# if this is a POST request we need to process the form data
	print (request.method)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:

		form = NameForm(data = request.POST)
		# check whether it's valid:
		print(form.is_valid())
	#	if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
		#tag = request.POST.get('Tag_Name','')
		tag = form['tag_name'].data;
		creator = form['creator'].data;
		#creator = request.POST.get('creator','')
		tag_obj = Tag(tag=tag,creator=creator)
		tag_obj.save()
		print (1111111111111111111)
		# redirect to a new URL:
		return render(request, 'fume/'+ game_id + '.html', {'tag_id':game_id})

	# if a GET (or any other method) we'll create a blank form
	#else:
	#	return render(request, 'fume/'+ game_id + '.html', {'tag_id':game_id})

	