from django.shortcuts import render,redirect
from . import forms
def index(request):
    form=forms.Employee()
    if request.method=='POST':
        form=forms.Employee(request.POST)
        msg='We have recieved this form once again'
        if form.is_valid():
         msg=msg+"Form is Valid"
    else:
      msg='Welcome for First time'
    return render(request,'index.html',{'msg':msg,'form':form})