import django


from django.shortcuts import render
from django.http import HttpResponse
from ..decorator import user_authenticated
from backend.models import user
@user_authenticated
def Threat_by(request):
    return render(request, 'templates/threat_by.html')