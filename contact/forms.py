from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    # Honeypot anti-spam
    website_hp = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom@exemple.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+226 XX XX XX XX (facultatif)'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objet de votre message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Écrivez votre message ici...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('website_hp'):
            raise forms.ValidationError("Spam détecté.")
        return cleaned_data
