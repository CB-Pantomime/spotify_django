
from django.contrib import admin

# importing Artist model from models.py
from .models import Artist, Playlist, Song

# Register your models here.
# This line will add the model to the admin panel
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)

