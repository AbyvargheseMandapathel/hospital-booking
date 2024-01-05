from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    DOCTOR_CHOICES = [
        ("Dr. Arun", "Dr. Arun - General Medicine"),
        ("Dr. Thomas", "Dr. Thomas - General Surgery"),
        ("Dr. Anjali", "Dr. Anjali - Neurology"),
        ("Dr. Sreelakshmi", "Dr. Sreelakshmi - Pediatrics"),
    ]

    doc_name = forms.ChoiceField(choices=DOCTOR_CHOICES, label="Doctor")

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name': 'Patient Name',
            'p_phone': 'Patient Phone',
            'p_email': 'Patient Email',
            'booking_date': 'Booking Date',
            'doc_name': 'Doctor Name',
        }
