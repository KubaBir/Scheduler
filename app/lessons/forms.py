from core.models import Availability
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError


class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'id': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'value': '08:00', 'list': 'time', 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        if Availability.objects.filter(date=cleaned_data['date'], time=cleaned_data['time']).exists():
            raise ValidationError(
                "This lesson instance already exists", code="duplicate lesson")
        return cleaned_data


class JoinLessonForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = []
