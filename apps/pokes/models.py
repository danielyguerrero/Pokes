from __future__ import unicode_literals
from ..login.models import User
from django.db import models



#=======================================================================
#                     PokeManager
#=======================================================================

class PokeManager(models.Manager):
	def Poke(self, id, cur_id):
		try: #TRY
			userToPoke = User.objects.get(id=id)  # all users
			cur_User = User.objects.get(id=cur_id) # current user
			Poke.objects.create(poker=cur_User, poked=UserToPoke)
		except: #EXCEPT
			print "No user with id {}". format(id)

#=======================================================================
#                     Poke Class
#=======================================================================
class Poke(models.Model):

#made two foreign keys becuase i want the functionality to be separate from the login app
	poked = models.ForeignKey(User, related_name="pokes_gotten")
	poker = models.ForeignKey(User, related_name="pokes_made")
	created_at = models.DateTimeField(auto_now_add=True)

	objects =PokeManager