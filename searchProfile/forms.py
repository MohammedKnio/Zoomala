from django import forms


class ComposeForm(forms.Form):
    q = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control", "type":"text" , "aria-label":"Search for a profile", "placeholder": "Search for a profile", }
                )
            )