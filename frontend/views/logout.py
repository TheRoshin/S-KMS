from django.shortcuts import redirect


def userLogout(request): 
    try: 
        del request.session['token']
        return redirect('/user')
    except KeyError: 
        pass 