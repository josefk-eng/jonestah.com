from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import ContactMessage
from countable_field.widgets import CountableWidget


class ContactMessageForm(ModelForm):

    def __init__(self,*args, **kwargs):
        super(ContactMessageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContactMessage
        fields = "__all__"
        widgets = {
            'subject': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'subject',
                    'name': 'subject'
                }
            ),
            'message': CountableWidget(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'row': '10',
                    'data-count': 'characters',
                    'data-min-count': 0,
                    'data-max-count': 1000,
                    'data-count-direction': 'down'
                }
            ),
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'name',
                    'id': 'name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'name': 'email',
                    'id': 'email'
                }
            )
        }

