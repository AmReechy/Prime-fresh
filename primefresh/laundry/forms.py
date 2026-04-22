from django import forms
from .models import Booking, ContactMessage
from django.utils import timezone


class BookingForm(forms.ModelForm):
    preferred_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': timezone.now().date().isoformat()}
        )
    )

    class Meta:
        model = Booking
        fields = [
            'full_name', 'email', 'phone', 'address',
            'service_type', 'preferred_date', 'preferred_slot',
            'estimated_items', 'needs_pickup', 'needs_delivery',
            'special_instructions',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '080XXXXXXXX'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Pickup address (street, area, city)'}),
            'special_instructions': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Any special instructions, fabric sensitivities, stain details...'
            }),
            'estimated_items': forms.NumberInput(attrs={'placeholder': 'e.g. 10', 'min': 1}),
        }

    def clean_preferred_date(self):
        date = self.cleaned_data.get('preferred_date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("Please select a future date.")
        return date


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '080XXXXXXXX (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'What is this regarding?'}),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Tell us how we can help you...'
            }),
        }
