

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.views import View


# Here we are looking into the models.py file and importing the Artist, Song, and       Playlist classes
# from the file
from .models import Artist, Song, Playlist 


# ****************************************************
# Create your views here.
class Home(TemplateView):
    # now using TemplateView instead of rendering basic HttpResponse
    #  BUT WAIT! What happened to the get method?
    # When we are using a template view we do not need to define the get method. Django has handled that for us. Thanks Django!
    template_name = "home.html"

    # Addings the playlists as context 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context 



class About(TemplateView):  
    template_name = "about.html"
    

class ArtistList(TemplateView):
    template_name = "artist_list.html"
    
    # this method is named obvious and nice and it is built into 
    # all template class.
    # We will be passing key word arguments, is that what the artists list is going in as? 
    def get_context_data(self, **kwargs):

        # HELP PLZ: Don't really understand this here
        # Base implementation first to get a context, literally,
        # then using keyword CONTEXT to implement said context?
        # How can we say this in simpler terms?
        # Is this recursion? 
        context = super().get_context_data(**kwargs)
        # var called name equal to value of request GET method w/ query parameter "name"?
        name = self.request.GET.get("name")
        # If a query exists we will filter by name
        if name != None:
            # no longer equal the list of artists now equal to 
            # Artist class objects w/ filter method
            # and that query is Case-INsensitive w/__icontains 
            # the 'name' preceding the __icontains is place keeper for our variable?
            context["artists"] = Artist.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            # add in a QuerySet of all the artists * I think I get this tho
            # Is this passing back to what is above? 
            # Here we are using the model to query the databse for us
            context["artists"] = Artist.objects.all()
            # default header for not searching 
            context["header"] = "Trending Artists"
        return context 


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    success_url = "/artists/"


class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"
    success_url = "/artists/"


class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"


class SongCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        artist = Artist.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, artist=artist)

        return redirect('artist_detail', pk=pk)









# class Song:
#     def __init__(self, title, group):
#         self.title = title
#         self.group = group

# songs = [
#     Song("title of song", "name of group"),
#     Song("title of song", "name of group"),
#     Song("title of song", "name of group"),
#     Song("title of song", "name of group"),
#     Song("title of song", "name of group"),
#     Song("title of song", "name of group"),
# ]


# class SongList(TemplateView):
#     template_name = "song_list.html"

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)
#         context["songs"] = songs
#         return context 


