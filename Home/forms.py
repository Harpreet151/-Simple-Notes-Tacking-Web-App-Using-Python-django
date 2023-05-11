from django import forms
from .models import Notes
 
class detailsform(forms.ModelForm):
    class Meta:
        model=Notes
        fields="__all__"
        exclude = ("user",)