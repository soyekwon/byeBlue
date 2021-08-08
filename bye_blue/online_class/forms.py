from django import forms
from .models import Online

class OnlineForm(forms.ModelForm):

   class Meta:
       model = Online
       fields = ['title', 'content'] 
