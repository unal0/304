from django import forms
from .models import Appointment2

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment2
        fields = [
            'AppointmentID',
            'AppointmentDate',
            'AppointmentTime',
            'Patient_PatientID',
            'Doctor_DoctorID',
            'Prescription_Prescription_Code',
            'Bill_BillID',
            'Test_TestID'
        ]
        widgets = {
            'Prescription_Prescription_Code': forms.Select(attrs={'required': False}),
        }

    def print_form(self):
        for field_name, value in self.cleaned_data.items():
            print(f"{field_name}: {value}")




