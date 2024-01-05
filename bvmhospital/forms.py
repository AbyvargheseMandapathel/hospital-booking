# forms.py
from django import forms
from .models import Booking, Doctors

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    doctor_choices = [(doctor.id, f"{doctor.doc_name} - {doctor.doc_spec}") for doctor in Doctors.objects.all()]

    doc_name = forms.ChoiceField(choices=doctor_choices, label="Doctor")

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

    def clean_doc_name(self):
        doctor_id = self.cleaned_data['doc_name']
        return Doctors.objects.get(id=doctor_id)
