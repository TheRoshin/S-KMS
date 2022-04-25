from django.shortcuts import get_object_or_404, redirect, render

from frontend.decorator import user_authenticated
from ..forms import updatePasswordForm
from backend.models import profile, user

@user_authenticated
def updatePassword(request, slug):
    pro = get_object_or_404(profile, slug=slug)
    use = user.objects.get(username = request.session['token'])
    form = updatePasswordForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            if form.cleaned_data['pass_word'] == use.password:
                use.password = form.cleaned_data['pass_word2']  
                use.save()
                return redirect('/user')
            else:
             return render(request, 'templates/updatePassword.html', {'form': form, 'pro': pro ,'message': 'password is not correct'})   
           
    return render(request, 'templates/updatePassword.html', {'form': form, 'pro': pro})