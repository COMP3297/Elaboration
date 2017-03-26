from django.contrib import admin

# Register your models here.

from .models import Game
from .models import User
from .models import Tagging
from .models import Tag
from .models import Purchase

admin.site.register(Game)
admin.site.register(User)
admin.site.register(Tagging)
admin.site.register(Tag)
admin.site.register(Purchase)