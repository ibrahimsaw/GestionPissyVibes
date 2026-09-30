from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    # Honeypot anti-spam field (hidden via CSS)
    website_hp = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = EventRegistration
        fields = ['first_name', 'last_name', 'phone', 'email', 'number_of_people', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+226 XX XX XX XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom@exemple.com'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Informations complémentaires ou questions (facultatif)'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('website_hp'):
            raise forms.ValidationError("Spam détecté.")
        return cleaned_data
