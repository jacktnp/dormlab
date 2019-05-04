from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Payment, Reporting

class GuestPaymentForm(forms.ModelForm):
    bill_attr = {'type' :"file", 'class': "custom-file-input"}
    date_attr = {'type': "datetime-local", 'class': "form-control"}
    desc_attr = {'class': "form-control" ,'rows': "3"}


    bill_picture = forms.ImageField(
        widget=forms.TextInput(attrs=bill_attr))
    payment_datetime = forms.DateTimeField(
        widget=forms.TextInput(attrs=date_attr))
    payment_desc = forms.CharField(widget=forms.Textarea(attrs=desc_attr))


    class Meta:
        model = Payment
        exclude = ['payment_confirm', 'payment_guest_id']


class GuestReportForm(forms.ModelForm):
    desc_attr = {'class': "form-control", 'id': "detail", 'rows': "3"}

    report_desc = forms.CharField(widget=forms.Textarea(attrs=desc_attr))

    class Meta:
        model = Reporting
        exclude = ['report_date', 'report_type_type_id', 'room_room_id']

