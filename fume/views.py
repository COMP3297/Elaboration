from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from fume.models import Game,Cart,Tag,User
from fume.forms import NameForm
from fume.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from fume.forms import SignUpForm


	
def featured(request):
	return render(request, 'fume/featured.html', {})
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def games(request, game_id):
	game = Game.objects.get(game_id=game_id)
	tags = Tag.objects.filter(game=game).all()
	return render(request, 'fume/gamePage.html', {'tag_id':game_id, 'tags':tags})
	
def purchase(request, game_id):
	print("purchasing")
	newgame=Game.objects.get(game_id=game_id)
	user = User.objects.get(userId='123')
	this_cart = Cart.objects.get(user = user)
	this_cart.addGame(newgame)
	amount = this_cart.game.all().count()
	games = this_cart.game.all()
	totalAmount = this_cart.getTotal()
	return render(request, 'fume/purchase.html', {'games': games, 'amount': amount, 'totalAmount': totalAmount})

def purchaseAll(request):
	user = User.objects.get(userId='123')
	Cart.objects.get(user=user).delete()
	new_cart=Cart(user=user)
	new_cart.save()
	return render(request, 'fume/featured.html', {})

def tagedit(request, game_id):
	tag_id=game_id
	return render(request, 'fume/tag.html', {'tag_id':game_id})
	

def addtag(request, game_id):
	print ("adding tag")
# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:

		form = NameForm(data = request.POST)
		# check whether it's valid:
		print(form.is_valid())
		if form.is_valid():
				# process the data in form.cleaned_data as required
				# ...
			
			tag = form['tag_name'].data;
			creator = form['creator'].data;
			this_game = Game.objects.get(game_id=game_id)
			#creator = request.POST.get('creator','')
			tag_obj = Tag(tag=tag,creator=creator,game=this_game)
			tag_obj.save()
			print ("tag added")	
			
			# redirect to a new URL:
		return redirect('games',game_id=game_id)


	# if a GET (or any other method) we'll create a blank form
	else:
		return redirect('games',game_id=game_id)

	