from django import forms
from django.forms import ModelForm
from .models import Flower
class FlowerForm(ModelForm):
    # title = forms.CharField(label='Title', widget= forms.TextInput(attrs={'class': 'form-control '}))
    class Meta:
        model = Flower
        # fields = ['title']
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image_field'})
        }
        labels = {
            'title': '名稱',
            'description': '敘述',
            'slug': '代號',
            'category': '類別',
            'tags': '標籤',
            'image': '圖片'
        }