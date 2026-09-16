from django import forms

class userForm(forms.Form):
   name=forms.CharField()
   phone=forms.CharField()
   city=forms.CharField()
   course=forms.CharField()