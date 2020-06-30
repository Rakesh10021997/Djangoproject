from django import forms

class StudentRegistration(forms.Form):
    Name=forms.CharField()
    Marks=forms.IntegerField()
