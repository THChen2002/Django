from django import forms

class PostForm(forms.Form):
    userName = forms.CharField(max_length = 50, initial='', required = True)
    userPassword = forms.CharField(max_length = 50, initial='', required = True)
    userFirstName = forms.CharField(max_length = 50, initial='', required = True)
    userLastName = forms.CharField(max_length = 50, initial='', required = True)
    userEmail = forms.CharField(max_length = 50, initial='', required = True)