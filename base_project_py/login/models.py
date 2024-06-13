# Create your models here.
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    PatientID = models.IntegerField(db_column='PatientID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45, default='123')

    class Meta:
        db_table = 'Patient'

class Doctor(models.Model):
    DoctorID = models.IntegerField(db_column='DoctorID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45)

    class Meta:
        db_table = 'Doctor'

class Admin(models.Model):
    AdminID = models.IntegerField(db_column='AdminID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45)

    class Meta:
        db_table = 'Admin'

class Receptionist(models.Model):
    ReceptionistID = models.IntegerField(db_column='ReceptionistID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45)

    class Meta:
        db_table = 'Receptionist'

class Pharmacist(models.Model):
    PharmacistID = models.IntegerField(db_column='PharmacistID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45)

    class Meta:
        db_table = 'Pharmacist'

class LabAssistant(models.Model):
    LabAssistantID = models.IntegerField(db_column='LabAssistantID', primary_key=True)
    Username = models.CharField(db_column='Username', max_length=45)
    Name = models.CharField(db_column='Name', max_length=45)
    Surname = models.CharField(db_column='Surname', max_length=45)
    Phone = models.CharField(db_column='Phone', max_length=45)
    Password = models.CharField(db_column='Password', max_length=45)

    class Meta:
        db_table = 'LabAssistant'








class Insurance2(models.Model):
    IsuranceNumber = models.IntegerField(primary_key=True, db_column='IsuranceNumber')
    InsuranceCoverage = models.DecimalField(max_digits=5, decimal_places=2, null=True, db_column='InsuranceCoverage')
    InsuranceCompany = models.CharField(max_length=45, null=True, db_column='InsuranceCompany')

    class Meta:
        db_table = 'Insurance2'

class Patient2(models.Model):
    PatientID = models.IntegerField(primary_key=True, db_column='PatientID')
    Patient_Phone = models.IntegerField(null=True, db_column='Patient_Phone')
    Patient_Gender = models.CharField(max_length=45, null=True, db_column='Patient_Gender')
    PatientName = models.CharField(max_length=45, null=True, db_column='PatientName')
    PatientSurname = models.CharField(max_length=45, null=True, db_column='PatientSurname')
    Password = models.CharField(max_length=128, default='default_password', db_column='Password')  # Add a default value here
    Insurance_IsuranceNumber = models.ForeignKey(Insurance2, on_delete=models.CASCADE, db_column='Insurance_IsuranceNumber')

    class Meta:
        db_table = 'Patient2'

class Department2(models.Model):
    DepartmentCode = models.CharField(max_length=10, primary_key=True, db_column='DepartmentCode')
    DepartmentName = models.CharField(max_length=120, null=True, db_column='DepartmentName')

    class Meta:
        db_table = 'Department2'

class Doctor2(models.Model):
    DoctorID = models.IntegerField(primary_key=True, db_column='DoctorID')
    Doctor_Name = models.CharField(max_length=45, null=True, db_column='Doctor_Name')
    Doctor_Surname = models.CharField(max_length=45, null=True, db_column='Doctor_Surname')
    Doctor_Address = models.CharField(max_length=45, null=True, db_column='Doctor_Address')
    Doctor_Title = models.CharField(max_length=45, null=True, db_column='Doctor_Title')
    ExaminationPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='ExaminationPrice')
    Department_DepartmentCode = models.ForeignKey(Department2, on_delete=models.CASCADE, db_column='Department_DepartmentCode')

    class Meta:
        db_table = 'Doctor2'

class DoctorSchedule2(models.Model):
    Date = models.DateField(null=True, db_column='Date')
    Time = models.TimeField(null=True, db_column='Time')
    Availability = models.CharField(max_length=45, null=True, db_column='Availability')
    Doctor_DoctorID = models.ForeignKey(Doctor2, on_delete=models.CASCADE, db_column='Doctor_DoctorID')

    class Meta:
        db_table = 'DoctorSchedule2'

class Prescription2(models.Model):
    MedicineName = models.CharField(max_length=120, null=True, db_column='MedicineName')
    Prescription_Date = models.DateField(null=True, db_column='Prescription_Date')
    PresriptionCost = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='PresriptionCost')
    Prescription_Code = models.CharField(max_length=45, primary_key=True, db_column='Prescription_Code')
    Doctor_DoctorID = models.ForeignKey(Doctor2, on_delete=models.CASCADE, db_column='Doctor_DoctorID')
    Patient_PatientID = models.ForeignKey(Patient2, on_delete=models.CASCADE, db_column='Patient_PatientID')
    Patient_Insurance_IsuranceNumber = models.ForeignKey(Insurance2, on_delete=models.CASCADE, db_column='Patient_Insurance_IsuranceNumber')

    class Meta:
        db_table = 'Prescription2'

class Bill2(models.Model):
    BillID = models.IntegerField(primary_key=True, db_column='BillID')
    BillDate = models.DateField(null=True, db_column='BillDate')

    class Meta:
        db_table = 'Bill2'

class TestResult2(models.Model):
    TestResultID = models.IntegerField(primary_key=True, db_column='TestResultID')
    Value = models.DecimalField(max_digits=10, decimal_places=2, db_column='Value')

    class Meta:
        db_table = 'TestResult2'

class Test2(models.Model):
    TestID = models.IntegerField(primary_key=True, db_column='TestID')
    TestName = models.CharField(max_length=200, null=True, db_column='TestName')
    NormalValue = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='NormalValue')
    Diagnosis = models.CharField(max_length=45, null=True, db_column='Diagnosis')
    TestUnitPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='TestUnitPrice')
    TestResult_TestResultID = models.ForeignKey(TestResult2, on_delete=models.CASCADE, db_column='TestResult_TestResultID')
    SpecimenType = models.CharField(max_length=200, null=True, db_column='SpecimenType')

    class Meta:
        db_table = 'Test2'

class Appointment2(models.Model):
    AppointmentID = models.IntegerField(primary_key=True, db_column='AppointmentID')
    AppointmentDate = models.DateField(db_column='AppointmentDate')
    AppointmentTime = models.TimeField(db_column='AppointmentTime')
    Patient_PatientID = models.ForeignKey(Patient2, on_delete=models.CASCADE, db_column='Patient_PatientID')
    Doctor_DoctorID = models.ForeignKey(Doctor2, on_delete=models.CASCADE, db_column='Doctor_DoctorID')
    Prescription_Prescription_Code = models.ForeignKey(Prescription2, on_delete=models.CASCADE, db_column='Prescription_Prescription_Code', null=True, blank=True)
    Bill_BillID = models.ForeignKey(Bill2, on_delete=models.CASCADE, db_column='Bill_BillID', null=True, blank=True)
    Test_TestID = models.ForeignKey(Test2, on_delete=models.CASCADE, db_column='Test_TestID', null=True, blank=True)

    class Meta:
        db_table = 'Appointment2'

class Medicines2(models.Model):
    MedicineID = models.IntegerField(primary_key=True, db_column='MedicineID')
    Medicine_Quantity = models.IntegerField(null=True, db_column='Medicine_Quantity')
    Medicine_Name = models.CharField(max_length=120, null=True, db_column='Medicine_Name')
    ExpiryDate = models.DateField(null=True, db_column='ExpiryDate')
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='Price')

    class Meta:
        db_table = 'Medicines2'

class Pharmacist2(models.Model):
    PharmacistID = models.IntegerField(primary_key=True, db_column='PharmacistID')
    PharmacistName = models.CharField(max_length=45, null=True, db_column='PharmacistName')
    PharmacistSurname = models.CharField(max_length=45, null=True, db_column='PharmacistSurname')
    Pharmacist_Phone = models.IntegerField(null=True, db_column='Pharmacist_Phone')

    class Meta:
        db_table = 'Pharmacist2'

class Patient_has_Doctor2(models.Model):
    Patient_PatientID = models.ForeignKey(Patient2, on_delete=models.CASCADE, db_column='Patient_PatientID')
    Doctor_DoctorID = models.ForeignKey(Doctor2, on_delete=models.CASCADE, db_column='Doctor_DoctorID')

    class Meta:
        db_table = 'Patient_has_Doctor2'
        unique_together = (('Patient_PatientID', 'Doctor_DoctorID'),)

class Medicines_has_Pharmacist2(models.Model):
    Medicines_MedicineID = models.ForeignKey(Medicines2, on_delete=models.CASCADE, db_column='Medicines_MedicineID')
    Pharmacist_PharmacistID = models.ForeignKey(Pharmacist2, on_delete=models.CASCADE, db_column='Pharmacist_PharmacistID')

    class Meta:
        db_table = 'Medicines_has_Pharmacist2'
        unique_together = (('Medicines_MedicineID', 'Pharmacist_PharmacistID'),)

class Prescription_has_Medicines2(models.Model):
    Prescription_Prescription_Code = models.ForeignKey(Prescription2, on_delete=models.CASCADE, db_column='Prescription_Prescription_Code')
    Medicines_MedicineID = models.ForeignKey(Medicines2, on_delete=models.CASCADE, db_column='Medicines_MedicineID')

    class Meta:
        db_table = 'Prescription_has_Medicines2'
        unique_together = (('Prescription_Prescription_Code', 'Medicines_MedicineID'),)

class Specimen2(models.Model):
    SpecimenID = models.IntegerField(primary_key=True, db_column='SpecimenID')
    SpecimentType = models.CharField(max_length=200, null=True, db_column='SpecimentType')

    class Meta:
        db_table = 'Specimen2'

class Specimen_has_Test2(models.Model):
    Specimen_SpecimenID = models.ForeignKey(Specimen2, on_delete=models.CASCADE, db_column='Specimen_SpecimenID')
    Test_TestID = models.ForeignKey(Test2, on_delete=models.CASCADE, db_column='Test_TestID')
    Test_TestResult_TestResultID = models.ForeignKey(TestResult2, on_delete=models.CASCADE, db_column='Test_TestResult_TestResultID')

    class Meta:
        db_table = 'Specimen_has_Test2'
        unique_together = (('Specimen_SpecimenID', 'Test_TestID', 'Test_TestResult_TestResultID'),)
