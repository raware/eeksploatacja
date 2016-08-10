from django import forms
from .models import Zjazd


class ZjazdForm(forms.ModelForm):

    class Meta:
        model = Zjazd
        #fields = ()
        exclude = ()
        widgets = {
        	'data': forms.DateInput(),
        	'czas': forms.TimeInput(),
            #'data_godzina': forms.DateTimeInput(attrs={'class':'datepicker'}),
        }