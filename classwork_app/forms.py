from django import forms
from classwork_app.models import ContactModel
from django.core import validators

class BasicForm(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)

class ContactForm(forms.Form):
    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'
    NAIRALAND = 'nairaland'
    TWITTER = 'twitter'
    CHOOSE = ''
    REFERE_FIELD = [
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (NAIRALAND, 'Nairaland'),
        (TWITTER, 'Twitter'),
        (CHOOSE, 'Please Choose'),
    ]

    MALE = 'male'
    FEMALE = 'female'
    GENDER_FIELD = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Phone'}), max_length=11, help_text='Please make your is equal to 11')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}), label='Company Email')
    verify_email = forms.EmailField(label='Very Company Email', disabled=True)
    referer = forms.CharField(widget=forms.Select(choices=REFERE_FIELD), required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_FIELD))
    image = forms.ImageField(widget=forms.ClearableFileInput, required=False)
    message = forms.CharField(widget=forms.Textarea)

def check_for_c(value):
    if value[0].lower() != 'c':
        raise forms.ValidationError('Please name must start with c')

class ContactUsForm(forms.ModelForm):
    botcacher = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])
    name = forms.CharField(validators=[check_for_c], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
    class Meta():
        model = ContactModel
        fields = '__all__'
        widgets = {
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Phone'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Subject'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
    
    def clean_subject(self):
        subject1 = self.cleaned_data['subject']
        if 'hello' not in subject1:
            raise forms.ValidationError("There must be 'hello' in subject field ")



