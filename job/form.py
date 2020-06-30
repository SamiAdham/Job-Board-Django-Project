from django import forms
from .models import Apply, Job

'''
class Apply_Form(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']
'''

class Apply_Form(forms.ModelForm):
    """Form definition for Apply_."""

    class Meta:
        """Meta definition for Apply_form."""

        model = Apply
        fields = ('name','email','website','cv','cover_letter')



class Add_job(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Job
        fields = '__all__'
        exclude =['slug']


