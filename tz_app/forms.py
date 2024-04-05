from django import forms
from tz_app.models import Account

class StartForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username']
        labels = {'text': ''}
    

