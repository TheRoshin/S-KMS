from django.shortcuts import get_object_or_404, redirect, render

from frontend.decorator import user_authenticated
from ..forms import commentForm
from backend.models import comment, postQus, user
@user_authenticated
def post_detail(request, slug):
    post = get_object_or_404(postQus, slug=slug)
    comments = comment.objects.filter(posted = post).order_by('comment_date')
    User = request.session['token']
    User2 = user(username = request.session['token']).username
    post.view += 1
    post.save()
    new_comment = None
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            new_comment = comment(comment_text = form.cleaned_data['comment_text'], posted = post, comment_by = user(username = request.session['token']))
            new_comment.save()
            form = commentForm()
    else:
        form = commentForm()
    return render(request, 'postDetail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'form': form, 'User': User, 'user2': User2})