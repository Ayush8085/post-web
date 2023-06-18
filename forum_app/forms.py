from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Description'}))

    class Meta:
        model = Post
        fields = ['title', 'description']