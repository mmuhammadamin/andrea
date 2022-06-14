from django import forms

from .models import ContactForm, Comment, Comment_single, Contact_Form_single


class Contact_form(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(Contact_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'

        self.fields['message'].widget.attrs['placeholder'] = 'Message'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = '__all__'

        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

class CommentForm_single(forms.ModelForm):
    class Meta:
        model = Comment_single

        fields = '__all__'

        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(CommentForm_single, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

class Contact_form_single(forms.ModelForm):
    class Meta:
        model = Contact_Form_single
        fields = '__all__'
        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(Contact_form_single, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
