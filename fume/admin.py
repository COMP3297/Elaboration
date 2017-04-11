from django.contrib import admin

# Register your models here.

from .models import Game , Tagging , Tag, Purchase, Cart, GameImage


admin.site.register(Game)
admin.site.register(Tagging)
admin.site.register(Tag)
admin.site.register(Purchase)
admin.site.register(Cart)
admin.site.register(GameImage)