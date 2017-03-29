from django import forms

class NameForm(forms.Form):
    Tag_Name = forms.CharField(label='Tag_Name', max_length=100)