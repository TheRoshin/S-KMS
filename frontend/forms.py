from django import forms

from backend.models import profile,user

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
        label= 'Describe little more',
        max_length=1000,
        widget= forms.Textarea()
    )
class SignupForm(forms.Form):
    first_name = forms.CharField(
        label= 'First name',
        max_length= 50
    )
    last_name = forms.CharField(
        label= 'Last name',
        max_length= 50
    )
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
    pass_word2 = forms.CharField(
         max_length= 50,
         label = 'Retype Password',
         widget= forms.PasswordInput()
         )     

class commentForm(forms.Form):
    comment_text = forms.CharField(
        max_length=1000,
        label='Type Something',
        widget= forms.Textarea()
    )

class updatePasswordForm(forms.Form):
        pass_word = forms.CharField(
         max_length= 50,
         label = 'Current Password',
         widget= forms.PasswordInput()
         )
        pass_word2 = forms.CharField(
         max_length= 50,
         label = 'New Password',
         widget= forms.PasswordInput()
         )  

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['pic', 'bio']    
