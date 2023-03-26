from django import forms

class PostForm(forms.Form):
    stdName = forms.CharField(max_length = 50, initial='', required = True)
    stdID = forms.CharField(max_length = 10, initial='', required = True)
    stdSex = forms.CharField(max_length = 2, initial='M', required = True)
    stdBirth = forms.DateField(initial='', required = False)
    stdPhone = forms.CharField(max_length = 50, initial = '', required = False)