from django import forms
from .forms import *


# Create your forms here.
class address(forms.Form):
    line_first = forms.CharField(blank=False, null=False, max_length=200)
    line_second = forms.CharField(blank=True, null=True, max_length=200)
    city = forms.CharField(blank=True, null=True, max_length=50)
    state = forms.CharField(blank=True, null=True, max_length=50)
    pincode = forms.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.city


class hotel(forms.Form):
    hotel_type_choice = (
        ("AC", "AC"),
        ("NON-AC", "NON-AC"),
        ("AC + NON_AC", "AC + NON-AC"),
    )
    hotel_name = forms.CharField(max_length=50, blank=True, null=True)
    hotel_Address = forms.ForeignKey(address, on_delete=forms.CASCADE)
    hotel_type = forms.CharField(max_length=20, choices=hotel_type_choice)

    def __str__(self):
        return self.hotel_name
