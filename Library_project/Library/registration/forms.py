from django import forms
from .models import User

class UserForm(forms.ModelForm):
    phone_num = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    


    class Meta:
        model = User
        fields = ('name','email','username','password','phone_num')




