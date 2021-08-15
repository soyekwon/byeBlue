from django import forms
from django.forms.fields import Field
from .models import Online, Comment

class OnlineForm(forms.ModelForm):

   class Meta:
       model = Online
       fields = ['title', 'content'] 


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields =['text']
                
