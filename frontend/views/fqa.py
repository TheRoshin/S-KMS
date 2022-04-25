from django.shortcuts import render
from django.http import HttpResponse
from ..decorator import user_authenticated
from backend.models import user
@user_authenticated
def fqa(request):
    User = user(username = request.session['token']).username
    return render(request, 'templates/fqa.html', {'user': User})