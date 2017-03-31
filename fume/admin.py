from django.contrib import admin

# Register your models here.

from .models import Game , User, Tagging , Tag, Purchase, Cart


admin.site.register(Game)
admin.site.register(User)
admin.site.register(Tagging)
admin.site.register(Tag)
admin.site.register(Purchase)
admin.site.register(Cart)