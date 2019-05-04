from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Payment, Reporting, Guest, Employee
from django.contrib.auth.forms import UserCreationForm

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

class GuestCreateForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label="Your Username")
    # first password field
    # password1 = forms.CharField(label="Your Password")
    # confirm password field
    # password2 = forms.CharField(label="Repeat Your Password")
    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Surname")
    address = forms.CharField(label="Address")
    line = forms.CharField(label="Line")
    phone = forms.CharField(label="Phone")

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "username", "password1", "password2", "address", 'line', 'phone'
            )

    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
        return user
    # class Meta:
    #     model = User
    #     fields = ('email',)

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user

