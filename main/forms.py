from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'p-2 border border-gray-300 rounded w-full' , 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'p-2 border border-gray-300 rounded w-full' , 'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'class': 'p-2 border border-gray-300 rounded w-full',  'placeholder': 'Your Comment' ,'rows': 4}),
        }
