from django import forms

from .models import Comment, ContactForm
from ..travel.forms import CommentForm


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = '__all__'
        exclude = ('post', 'author')

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


# class Contact_form(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = '__all__'
#         exclude = ('post', 'author')
#
#     def __init__(self, *args, **kwargs):
#         super(Contact_form, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field_name
