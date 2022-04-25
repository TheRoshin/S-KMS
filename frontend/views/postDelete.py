from django.shortcuts import get_object_or_404, redirect, render

from frontend.decorator import user_authenticated
from ..forms import commentForm
from backend.models import comment, postQus, user
@user_authenticated
def post_delete(request, slug):
    post = get_object_or_404(postQus, slug=slug)
    
    if request.method == 'POST':
        comment.objects.filter(posted = post).delete()
        post.delete()
        return redirect('/user')   
    return render(request, 'delete.html', {'post': post})