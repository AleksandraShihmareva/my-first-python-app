from django import forms
from django.forms import DateField
from django.utils.translation import ugettext_lazy

from MyNotebook import settings
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NameForm(forms.ModelForm):
    class Meta:
        model = NoteNames
        exclude = ['']
        labels = { 'dateOfBirth': ugettext_lazy('Date Of Birth'),'phoneNumber': ugettext_lazy('Phone'),'userName': ugettext_lazy('Name')}
        widgets = {'dateOfBirth': DateInput()}
