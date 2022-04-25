from django.shortcuts import render,redirect
from ..forms import UserForm,SignupForm
from backend.models import user
from django.http import HttpResponse
from ..decorator import user_authenticated

@user_authenticated
def userLogin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                User = user.objects.get(username = form.cleaned_data['user_name'])
            except:
                return render(request, 'templates/index.html', {'form': form, 'message': 'user does not exist'}) 

            if User.password != form.cleaned_data['pass_word']:
                form = UserForm()
                return render(request, 'templates/index.html', {'form': form, 'message': 'password is not correct'}) 
            else:
                request.session['token']  = User.username
                return redirect('/user')  

        else:
            return render(request, 'templates/index.html', {'form': form, 'message': 'Form not valid'})    
    else:
        form = UserForm()
        return render(request, 'templates/index.html', {'form': form})
