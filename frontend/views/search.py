from django.shortcuts import render
from django.http import HttpResponse
from backend.models import postQus
from ..decorator import user_authenticated
@user_authenticated
def search(request):
    return render(request, 'templates/search.html')