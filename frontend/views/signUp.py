from re import U
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import SignupForm
from backend.models import user, profile

def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            #User = user.objects.get(username = form.cleaned_data['user_name'])
            #userEmail = user.objects.get(e_mail = form.cleaned_data['e_mail'])
            if form.cleaned_data['pass_word'] == form.cleaned_data['pass_word2']:
                try:
                    user.objects.get(username = form.cleaned_data['user_name'])
                    form = SignupForm()
                    return render(request, 'templates/signup.html', {'form': form, 'message': 'username already exist'})
                except user.DoesNotExist:
                    try:
                      user.objects.get(e_mail = form.cleaned_data['e_mail'])
                      form = SignupForm()
                      return render(request, 'templates/signup.html', {'form': form, 'message': 'e_mail is already used'})
                    except user.DoesNotExist:   
                        newUser = user(username = form.cleaned_data['user_name'],first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'], e_mail = form.cleaned_data['e_mail'], password = form.cleaned_data['pass_word'])
                        newUser.save()
                        newProfile = profile(owner = newUser, bio = 'No bio', slug = newUser.username)
                        newProfile.save()
                        return redirect('/user/login') 
            # if form.cleaned_data['pass_word'] != form.cleaned_data['pass_word2']:
            #     form = SignupForm()
            #     return render(request, 'templates/signup.html', {'form': form, 'message': 'password is not the same'}) 
            
            # if form.cleaned_data['e_mail'] == userEmail.e_mail:
            #     form = SignupForm()
            #     return render(request, 'templates/signup.html', {'form': form, 'message': 'e_mail is already used'})    
            # else:
            #     newUser = user(username = form.cleaned_data['user_name'], e_mail = form.cleaned_data['e_mail'], password = form.cleaned_data['pass_word'])
            #     newUser.save()
            #     return redirect('/user/login')
            else:
                 form = SignupForm()
                 return render(request, 'templates/signup.html', {'form': form, 'message': 'password is not the same'}) 
        else:
            return render(request, 'templates/signup.html', {'form': form, 'message': 'Form not valid'})    
    else:
        form = SignupForm()
        return render(request, 'templates/signup.html', {'form': form})
