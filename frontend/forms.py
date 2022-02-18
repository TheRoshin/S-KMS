from cProfile import label
from socket import fromshare
from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(
        label= 'username',
        max_length= 50
    )
    pass_word = forms.CharField(
         max_length= 50,
         label = 'Password',
         widget= forms.PasswordInput()
         )

class PostForm(forms.Form):
    post_title = forms.CharField(
        label = 'Post title',
        max_length= 20
    )
    post_text = forms.CharField(
        label= 'Type Something',
        max_length=1000
    )
class SignupForm(forms.Form):
    user_name = forms.CharField(
        label= 'username',
        max_length= 50
    )
    e_mail = forms.EmailField(
        label= 'E-mail',
        max_length= 254,
    )
    pass_word = forms.CharField(
         max_length= 50,
         label = 'Password',
         widget= forms.PasswordInput()
         )
