from django.contrib import admin
from django import forms
from .models import Review,RATE_CHOICES



class Rateform(forms.ModelForm):
       reviews=forms.CharField(widget=forms.Textarea(attrs={'class':"textarea is-warning"}),required=False)
       rate_by_design=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class':"select is-rounded"}), required=True)
       rate_by_usability=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class':"select is-rounded"}), required=True)
       rate_by_content=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class':"select is-rounded"}), required=True)

       class Meta:
           model=Review
           fields={'rate_by_design','rate_by_usability','rate_by_content','reviews'}