from django.views import generic
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


#list of all the songs
class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name ='all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):   #we create objects by creating class
	model = Album
	fields = ['artist', 'album_title','genre','album_logo']

class AlbumUpdate(UpdateView):   #we create objects by creating class
	model = Album
	fields = ['artist', 'album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')   #deletes an album and redirects to home page

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#clean normalised data
			username =form.cleaned_data['username']
			username =form.cleaned_data['password']
			user.set_password(password)
			user.save()
			#returns user object credentials are corr3ct
			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					request redirect('music:index')
				else echo "Not registered"

		return render(request, self.template_name, {'form': form})












 #from django.http import Http404
#from django.http import HttpResponse
#from django.shortcuts import render, get_object_or_404
#from .models import Album, Song
#we're gonna take http requests and send it back tto the server any webpage can be a http response

#def index(request):
#	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html') #by default django looks to templates folder so no path for templates defined
	#for album in all_albums:
	#	html += '<a href="' + url + '">' + album.album_title + '</a><br>'
	#context = {
	#	'all_albums' : all_albums,
	#}	#dictionary
	#return HttpResponse(template.render(context, request))
#	return render(request, 'music/index.html', {'all_albums' : all_albums})

#def detail(request, album_id):
	#try:
	#	album = Album.objects.get(pk=album_id)	
	#except Album.DoesNotExist:
	#	raise Http404("Album does not exist")
#	album = get_object_or_404(Album, pk=album_id)#replaces try get statement
#	return render(request, 'music/detail.html', {'album' : album})    

''' def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotexist):
		return render(request, 'music/detail.html', {
			'album' : album,
			'error_message': "You did not select a valid song", 
	selected_song.is_favorite = True
	selected_song.save()
	return render(request, 'music/detail.html', {'album' : album}) '''

