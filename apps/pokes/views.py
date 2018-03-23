from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import *
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

    cur_id = request.session['user_id']  # current user id

    cur_user = User.objects.get(id=cur_id)  #current user

    other_users = User.objects.exclude(id=cur_id)  #other users

    poked_by = cur_user.pokes_gotten.all().values("poker__name").annotate(Count('id')).order_by('-id__count')

    count = poked_by.count()

    context = {
        'cur_user': cur_user,
        'other_users': other_users,
        'poked_by': poked_by,
        'count': count,
    }
    return render(request, 'pokes/index.html', context)

# =================================================
# 						PROCESS
# =================================================

def addPoke(request, user_id):

    if 'user_id' in request.session:

        Poke.objects.userAddPoke(user_id, request.session['user_id'])

        return redirect(reverse("dashboard"))

    return redirect(reverse("landing"))


