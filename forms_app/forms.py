from django import forms
from django.core import validators


# create my own individual validation check
# def check_for_z(value):
    # if value[0].lower() != 'z':
        # raise forms.ValidationError('Name MUST start with Z!!!')


class FormName(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    verify_email = forms.EmailField(label = 'Enter your email again: ')
    text = forms.CharField(
        max_length=1000, required=False, widget=forms.Textarea)


# Add check for empty fields


# Add check for bots
  # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                # validators.MaxLengthValidator(0)])
# Add clean method for form
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email', ]
        vmail = all_clean_data['verify_email', ]

        if email != vmail:
            raise forms.ValidationError("Make sure both emails match.")