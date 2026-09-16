from django import forms

class userForm(forms.Form):
   name=forms.CharField()
   phone=forms.CharField()
   city=forms.ChoiceField(
    choices=[
      ("jalandhar", "Jalandhar"),
      ("Phagwara", "Phagwara"),
      ("Bareilly", "Bareilly"),
      ("Gwalior", "Gwalior"),
    ],
    required=False,
   )
   course=forms.MultipleChoiceField(choices=
                                   [("Python", "python"),
                                   ("Java", "java"),
                                   ("C++", "c++"),
                                   ("HTML", "html")],
                                   widget=forms.CheckboxSelectMultiple,
                                   required=False)
   gender=forms.ChoiceField(
    choices=[("male","Male") , ("female", "Female"),])
  