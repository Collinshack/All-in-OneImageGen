from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Image, CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'password1', 'password2']
        
        widgets= {'username': forms.TextInput(attrs={'class': 'form-control', 'id':"form3Example1", 'autofocus':"" }),
                  'name': forms.TextInput(attrs={'class': 'form-control', 'id':"form3Example2" }),
                  'email': forms.EmailInput(attrs={'class': 'form-control', 'id':"form3Example3" }),
                  'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id':"form3Example4" }),
                  'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id':"form3Example4" }),
                  
                  }

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('prompt', 'generated_image')
    
    
class ApiKeyForm(forms.Form):
    key = forms.CharField(max_length=16)
