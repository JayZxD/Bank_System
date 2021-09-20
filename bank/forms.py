from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ActionForm(forms.ModelForm):
    #username =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #email_id =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #contact_no =  forms.IntegerField(widget=forms.TextInput(attrs={'disabled':'True'}))
    class Meta:
        model = Deposit
        fields = ["username", "email_id", "contact_no", "amount"]

class TransactionForm(forms.ModelForm):
    #username =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #email_id =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #contact_no =  forms.IntegerField(widget=forms.TextInput(attrs={'disabled':'True'}))
    receiver = forms.ModelChoiceField(queryset=Users.objects.all(), initial=0)
    class Meta:
        model = Transact
        fields = ["username", "email_id", "contact_no", "amount","receiver"]