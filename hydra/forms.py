from django import forms
from django.contrib import admin
from localflavor.us.forms import USStateSelect



class BlastEmailForm(forms.Form):
    sender_display_name = forms.CharField(max_length=1024, label="Sender Display Name", widget=admin.widgets.AdminTextInputWidget)
    sender_email = forms.EmailField(max_length=1024, label="Sender Email", widget=admin.widgets.AdminTextInputWidget)
    subject = forms.CharField(max_length=1024, widget=admin.widgets.AdminTextInputWidget)
    message = forms.CharField(max_length=4096, widget=admin.widgets.AdminTextareaWidget)
    recipients_csv = forms.FileField(label="Recipients (CSV)")
    email_field = forms.CharField(max_length=128, label="Email Field", help_text="This gets autopopulated after you upload a CSV")


class GeoTargetForm(forms.Form):
    state = forms.CharField(initial="FL", max_length=2, label="State Abbreviation")
    geojson = forms.CharField(max_length=256000, widget=admin.widgets.AdminTextareaWidget, label="GeoJSON", help_text="You'll need to fetch this from Census.gov or Google or some such; ping Juliana or Jon. :D")
    primary_only = forms.BooleanField(initial=True, label="Primary Addresses Only", help_text="Recommended")