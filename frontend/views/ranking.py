from django.shortcuts import render
from django.http import HttpResponse
from backend.models import postQus,user
from ..decorator import user_authenticated
@user_authenticated
def rank(request):
    rankNum = 0
    User = user(username = request.session['token']).username
    queryset = postQus.objects.filter().order_by('-view')
    return render(request, 'templates/rank.html', {'list': queryset, 'num': rankNum, 'user': User})
    