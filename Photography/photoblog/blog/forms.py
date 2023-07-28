from django import forms
from .models import ContactSubmission

# Handle user input and validate data before saving it to database
class ContactForm(forms.ModelForm):
    class Meta:
        # Form based on ContactSubmission model
        model = ContactSubmission
        fields = ['name', 'phone_number', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes or additional attributes to form fields
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'required': True})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'required': True})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'required': True, 'type': 'email'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'required': True, 'rows': 4})