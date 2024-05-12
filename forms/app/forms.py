from django import forms

#creating a form 
class InputForm(forms.Form):
    first_name=forms.CharField(max_length = 200)
    last_name=forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text="Enter the Roll Number")
    password = forms.CharField(widget=forms.PasswordInput())
    
                               