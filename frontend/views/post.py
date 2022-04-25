
from time import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ..forms import PostForm
from backend.models import user, postQus
from ..decorator import user_authenticated
@user_authenticated
def PostQus(request):
    queryset = postQus.objects.filter(posted_by = user(username = request.session['token'])).order_by('-post_date')
    queryset2 = postQus.objects.filter().order_by('-post_date')
    User = user(username = request.session['token'])
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                postQus.objects.get(post_title = form.cleaned_data['post_title'])
                form = PostForm()
                return  render(request, 'templates/post.html', {'form': form, 'message': 'Post title already exist', 'user': User})
            except:    
                newPost = postQus(post_title = form.cleaned_data['post_title'], post_text = form.cleaned_data['post_text'],posted_by = user(username = request.session['token']))
                newPost.save()
                return redirect('/user/')
        else:
            return render(request, 'templates/post.html', {'form': form, 'message': 'Form not valid', 'user': User})

    else:
        form = PostForm()
        return render(request, 'templates/post.html', {'form': form, 'list': queryset, 'list2': queryset2, 'user': User})