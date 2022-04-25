from operator import imod
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from ..decorator import user_authenticated
from backend.models import profile, user

@user_authenticated
def profileView(request, slug):
    pro = get_object_or_404(profile, slug=slug)
    User = request.session['token']
    User2 = user(username = request.session['token']).username
    return render(request, 'profile.html', {'pro': pro, 'user': User, 'user2': User2})