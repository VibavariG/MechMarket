from django import forms

class EnquiryForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=True, label="First Name")
    lastname = forms.CharField(max_length=100, required=True, label="Last Name")
    org = forms.CharField(max_length=200, required=True, label="Organization")
    email = forms.EmailField(required=True, label="Email ID")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type your question here'}), required=True, label="Message")