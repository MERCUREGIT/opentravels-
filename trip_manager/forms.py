from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type= "date"
    
    def __init__(self, **kwargs):
        kwargs["format"] = "%d/%m/%y"
        super().__init__(**kwargs)
        
class TimeInput(forms.TimeInput):
    input_type= "time"

class CreateTrip(forms.ModelForm):
    origin = forms.CharField(widget=forms.TextInput, label='')
    destination = forms.CharField(widget=forms.TextInput, label='')
    agency = forms.CharField(widget=forms.TextInput, label='agency')
    description = forms.CharField(widget=forms.Textarea, label='')
    Date = forms.DateField(widget=forms.DateInput, label='')
    Time = forms.TimeField(widget=forms.TimeInput, label='')
    # thumb= forms.CharField(widget=forms.ImageField, label='')
    
    
    class Meta:
        model=models.trip_data
        fields=['origin','destination','Date','Time','agency','description','is_public' ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['Date'].widget = DateInput()
        self.fields['origin'].widget =  forms.TextInput(attrs={'placeholder':'Trip origin'})
        self.fields['agency'].widget =  forms.TextInput(attrs={'placeholder':'Trip agency'})
        self.fields['description'].widget =  forms.Textarea(attrs={'placeholder':'Trip description'})
        self.fields['destination'].widget =  forms.TextInput(attrs={'placeholder':'Trip destination'})
        self.fields['Time'].widget =  forms.TimeInput(attrs={'placeholder':'Trip Time'})
        self.fields['Time'].widget = TimeInput()
        

