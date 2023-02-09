from core.models import Availability
from django import forms


class LessonForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'id': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'value': '08:00', 'list': 'time', 'class': 'form-control'})
        }
