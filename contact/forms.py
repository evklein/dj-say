from django import forms

class MyContactForm(forms.Form):

    # Default form elements.
    # To add more refer to https://docs.djangoproject.com/en/1.10/topics/forms/
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
    # your_element = forms.CharField(required=True)

    # Uncomment to set labels for each element
    # def __init__(self, *args, **kwargs):
    #     super(MyContactForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['contact_name'].label = "Name"
    #     self.fields['contact_subject'].label = "Subject"
    #     self.fields['contact_email'].label = "Email Address"
    #     self.fields['content'].label = "Content"
