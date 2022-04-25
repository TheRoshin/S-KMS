from django.shortcuts import render
from django.http import HttpResponse
from backend.models import postQus,user,profile
from ..decorator import user_authenticated
@user_authenticated
def home(request):
    queryset = postQus.objects.filter(posted_by = user(username = request.session['token'])).order_by('-post_date')
    queryset2 = postQus.objects.filter().order_by('-post_date')
    User = user(username = request.session['token'])
    return render(request, 'templates/option.html', {'list': queryset, 'list2': queryset2, 'user': User})
    