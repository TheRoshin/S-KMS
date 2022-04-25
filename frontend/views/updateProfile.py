from django.shortcuts import get_object_or_404, redirect, render

from frontend.decorator import user_authenticated
from ..forms import UpdateProfileForm
from backend.models import profile

@user_authenticated
def updateProfile(request, slug):
    pro = get_object_or_404(profile, slug=slug)
    form = UpdateProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
           pro.pic = form.cleaned_data['pic'] 
           pro.bio = form.cleaned_data['bio'] 
           pro.save()
           return redirect('/user')
           
    return render(request, 'templates/updateProfile.html', {'form': form, 'pro': pro})