from django.shortcuts import render
from testapp import forms
# Create your views here.
def studentregisterview(request):
    form =forms.StudentRegistration()
    return render(request,'temptestapp/register.html',{'form':form})
