from __future__ import unicode_literals
from ..login.models import User
from django.db import models

#=======================================================================
#                     PokeManager
#=======================================================================

class PokeManager(models.Manager):

	def userAddPoke(self, id, cur_id):


	#user to poke (all users) check for their id
		userToPoke = User.objects.get(id=id)  

	# the current user 
		cur_User = User.objects.get(id=cur_id) 

	#creating a poke with the poker id and poked id
		poke = Poke.objects.create(poker=cur_User, poked=userToPoke)
		
		print poke
# if the id is not valid dispaly this


#=======================================================================
#                     Poke Class
#=======================================================================

class Poke(models.Model):

# User being poked with realted name pokes gotten
	poked = models.ForeignKey(User, related_name="pokes_gotten")

#User poking with realted name pokes made to other users
	poker = models.ForeignKey(User, related_name="pokes_made")

	created_at = models.DateTimeField(auto_now_add=True)

	objects = PokeManager()

