from django import forms

def check_size(value):
    if len(value)<6:
        raise forms.ValidationError('the password is too short')

class Employee(forms.Form):
    empid=forms.CharField(initial="First Name")
    empname=forms.CharField()
    email=forms.EmailField(help_text='enter your email')
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Address'}))
    contactno=forms.CharField(help_text='Enter your contact')
    password=forms.CharField(widget=forms.PasswordInput,validators=[check_size])
    re_password=forms.CharField(help_text='Re-enter password',widget=forms.PasswordInput)
