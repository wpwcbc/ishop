from django import forms
from django.contrib.auth.models import User
from ishopapp.models import Item

class ItemForm(forms.Form):
    Price = forms.DecimalField(max_digits=7, decimal_places=1)
    Textbook = 'Textbook'
    Instrument = 'Instrument'
    SchoolUniform = 'SchoolUniform'
    Stationary = 'Stationary'
    Others = 'Others'
    TYPE_CHOICE = (
        (Textbook, 'Textbook'),
        (Instrument, 'Instrument'),
        (SchoolUniform, 'SchoolUniform'),
        (Stationary, 'Stationary'),
        (Others, 'Others'),
    )
    Type = forms.ChoiceField(
        choices=TYPE_CHOICE
    )
    TradingLocation = forms.CharField(max_length=50)
    Name = forms.CharField(max_length=30)
    Description = forms.CharField(max_length=10000)
    Status = forms.BooleanField(required=False)

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']