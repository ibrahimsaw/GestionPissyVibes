from django import forms
from .models import VolunteerApplication

class VolunteerApplicationForm(forms.ModelForm):
    # Honeypot
    website_hp = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = VolunteerApplication
        fields = ['first_name', 'last_name', 'phone', 'email', 'age', 'city_neighborhood', 'interest_domain', 'availability', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+226 XX XX XX XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom@exemple.com (facultatif)'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 22', 'min': 12, 'max': 99}),
            'city_neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Pissy, Gounghin, Tampouy...'}),
            'interest_domain': forms.Select(attrs={'class': 'form-select'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Samedi matin, week-ends...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Partage avec nous tes motivations, tes talents ou tes idées !'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('website_hp'):
            raise forms.ValidationError("Spam détecté.")
        return cleaned_data
