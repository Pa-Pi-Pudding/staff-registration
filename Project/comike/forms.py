from django import forms
from comike.models import (
    GENDER_CHOICES,
    USE_CHOICES,
    ASSIGNMENT_HOLE_CHOICES,
    CARRIER0_SHIFT_CHOICES,
    ORGANIZATION_CHOICES,
)


class StaffDataForm(forms.Form):
    staff_name = forms.CharField(max_length=64)
    staff_name_kana = forms.CharField(max_length=200)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()
    )
    birth_day = forms.DateField(required=True)
    mail_address = forms.EmailField()
    phone_number = forms.CharField(max_length=10)
    e_name = forms.CharField(max_length=64)
    post_code = forms.CharField(max_length=7)
    address = forms.CharField(max_length=255)
    e_relationship = forms.CharField(max_length=10)
    e_phone_number = forms.CharField(max_length=10)
    join_day_0 = forms.BooleanField(False, widget=forms.CheckboxInput)
    join_day_1 = forms.BooleanField(False, widget=forms.CheckboxInput)
    join_day_2 = forms.BooleanField(False, widget=forms.CheckboxInput)
    join_day_3 = forms.BooleanField(False, widget=forms.CheckboxInput)
    assignment_1 = forms.ChoiceField(
        choices=ASSIGNMENT_HOLE_CHOICES,
        widget=forms.RadioSelect(),
    )
    assignment_2 = forms.ChoiceField(
        choices=ASSIGNMENT_HOLE_CHOICES,
        required=False,
        widget=forms.RadioSelect(),
    )
    partner = forms.CharField(max_length=64, required=False)  # charfield は固定長で、メモリを確保
    parking = forms.ChoiceField(
        choices=USE_CHOICES,
        required=False,
        widget=forms.RadioSelect)
    hotel = forms.ChoiceField(
            choices=USE_CHOICES,
            required=False,
            widget=forms.RadioSelect)
    password = forms.CharField(max_length=20)
    memo = forms.CharField(required=False)


class InformationForm(forms.Form):
    organization = forms.ChoiceField(
        choices=ORGANIZATION_CHOICES,
        widget=forms.RadioSelect,
    )
    content = forms.CharField()
    title = forms.CharField(max_length=255)


class WeatherForm(forms.Form):
    carrier_shift = forms.ChoiceField(choices=CARRIER0_SHIFT_CHOICES)
