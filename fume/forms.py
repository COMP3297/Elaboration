from django import forms

class NameForm(forms.Form):
    tag_name = forms.CharField(label='tag_name', max_length=100)
    creator = forms.CharField(label='creator', max_length=100)