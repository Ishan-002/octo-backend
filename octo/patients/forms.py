from django import forms
from django.forms import CharField, IntegerField, ChoiceField, FloatField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PatientRegistrationForm(UserCreationForm):
    CHOICESGENDER = [('1', 'Female'), ('2', 'Male'),
                     ('3', 'Prefer not to tell'), ]

    firstname = CharField(label="First Name", required=True, strip=True)
    lastname = CharField(label="Last Name", required=True, strip=True)
    phoneNo = IntegerField(label="Phone Number", required=True)
    email = CharField(label="Email Id", required=True, strip=True)
    gender = ChoiceField(choices=CHOICESGENDER,
                         widget=forms.RadioSelect, label="Gender")
    temperature = FloatField(label="Temperature", required=True,
                             widget=forms.NumberInput(attrs={'placeholder': 'Temp in F'}))
    bp = FloatField(label="Blood Pressure", required=True,
                    widget=forms.NumberInput(attrs={'placeholder': 'BP in mmHg'}))
    spo2 = FloatField(label="SpO2", required=True,
                            widget=forms.NumberInput(attrs={'placeholder': 'SpO2'}))
    rr = FloatField(label="R/R", required=True,
                    widget=forms.NumberInput(attrs={'placeholder': 'R/R'}))

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phoneNo', 'email',
                  'gender', 'temperature', 'bp', 'spo2', 'rr']