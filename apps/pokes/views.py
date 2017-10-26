from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Poke
from django.db.models import Count


# =================================================
# 						HELPERS FUNCTIONS
# =================================================

def current_user(request):
    return User.objects.get(id=request.session['user_id'])

# =================================================
# 						RENDER INDEX
# =================================================

def index(request):
    if not 'user_id' in request.session:
        return redirect(reverse("landing"))

    cur_id = request.session['user_id'] 

    cur_User = User.objects.get(id=cur_id)  #current user

    otherUsers = User.objects.exclude(id=cur_id)

    poked_by = cur_User.pokes_gotten.all().values("poker__name").annotate(Count('id')).order_by('-id__count')

    context = {
        'cur_User': cur_User,
        'otherUsers': otherUsers,
        'poked_by': poked_by
    }
    return render(request, 'pokes/index.html', context)

# =================================================
# 						PROCESS
# =================================================

def poke(request, id):

    if 'user_id' in request.session:

        cur_id = request.session['user_id']

        Poke.objects.Poke(id, cur_id)
        Poke.objects.poked()

        return redirect(reverse("dashboard"))

    return redirect(reverse("landing"))

