from django.db import models
from django.core.urlresolvers import reverse



#Red has primary key 1
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField();

	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk': self.pk })

	def __str__(self):
		return self.album_title + ' - ' + self.artist
		
class Song(models.Model):#is a part of album
	album = models.ForeignKey(Album, on_delete=models.CASCADE) #when album is deleted which song tht belonged,deletes the songs whose album is deleted
	file_type = models.CharField(max_length=10)#album being foreign key will connect to the column album,with the primary tkey in hand it will get the tiltle
	song_title = models.CharField(max_length=250)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title

