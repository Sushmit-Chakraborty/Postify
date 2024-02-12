from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postTitle','postContent']
        
        widgets = {
            'postContent': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'postTitle': 'Title',
            'postContent': 'Content',
        }