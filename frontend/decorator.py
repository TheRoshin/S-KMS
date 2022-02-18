from django.shortcuts import redirect




def user_authenticated(function): 
    def wrap(request, *args, **kwargs): 
        if 'token' not in request.session: 
            if request.path == '/user/login': 
                return function(request, *args, **kwargs)
            return redirect('/user/login')
        else: 
            if request.path == '/user/login': 
                return redirect('/user/')
            return function(request,*args,**kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
