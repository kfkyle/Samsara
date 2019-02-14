from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    user_email = forms.EmailField()
    phone = forms.CharField()
