# Generated by Django 4.2.1 on 2024-06-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient2",
            name="Password",
            field=models.CharField(
                db_column="Password", default="default_password", max_length=128
            ),
        ),
        migrations.AlterField(
            model_name="bill2",
            name="BillDate",
            field=models.DateField(db_column="BillDate", null=True),
        ),
        migrations.AlterField(
            model_name="bill2",
            name="BillID",
            field=models.IntegerField(
                db_column="BillID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="department2",
            name="DepartmentCode",
            field=models.CharField(
                db_column="DepartmentCode",
                max_length=10,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="department2",
            name="DepartmentName",
            field=models.CharField(
                db_column="DepartmentName", max_length=120, null=True
            ),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="DoctorID",
            field=models.IntegerField(
                db_column="DoctorID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="Doctor_Address",
            field=models.CharField(
                db_column="Doctor_Address", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="Doctor_Name",
            field=models.CharField(db_column="Doctor_Name", max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="Doctor_Surname",
            field=models.CharField(
                db_column="Doctor_Surname", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="Doctor_Title",
            field=models.CharField(db_column="Doctor_Title", max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="doctor2",
            name="ExaminationPrice",
            field=models.DecimalField(
                db_column="ExaminationPrice", decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="doctorschedule2",
            name="Availability",
            field=models.CharField(db_column="Availability", max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="doctorschedule2",
            name="Date",
            field=models.DateField(db_column="Date", null=True),
        ),
        migrations.AlterField(
            model_name="doctorschedule2",
            name="Time",
            field=models.TimeField(db_column="Time", null=True),
        ),
        migrations.AlterField(
            model_name="insurance2",
            name="InsuranceCompany",
            field=models.CharField(
                db_column="InsuranceCompany", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="insurance2",
            name="InsuranceCoverage",
            field=models.DecimalField(
                db_column="InsuranceCoverage", decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="insurance2",
            name="IsuranceNumber",
            field=models.IntegerField(
                db_column="IsuranceNumber", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="medicines2",
            name="ExpiryDate",
            field=models.DateField(db_column="ExpiryDate", null=True),
        ),
        migrations.AlterField(
            model_name="medicines2",
            name="MedicineID",
            field=models.IntegerField(
                db_column="MedicineID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="medicines2",
            name="Medicine_Name",
            field=models.CharField(
                db_column="Medicine_Name", max_length=120, null=True
            ),
        ),
        migrations.AlterField(
            model_name="medicines2",
            name="Medicine_Quantity",
            field=models.IntegerField(db_column="Medicine_Quantity", null=True),
        ),
        migrations.AlterField(
            model_name="medicines2",
            name="Price",
            field=models.DecimalField(
                db_column="Price", decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="patient2",
            name="PatientID",
            field=models.IntegerField(
                db_column="PatientID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="patient2",
            name="PatientName",
            field=models.CharField(db_column="PatientName", max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="patient2",
            name="PatientSurname",
            field=models.CharField(
                db_column="PatientSurname", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="patient2",
            name="Patient_Gender",
            field=models.CharField(
                db_column="Patient_Gender", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="patient2",
            name="Patient_Phone",
            field=models.IntegerField(db_column="Patient_Phone", null=True),
        ),
        migrations.AlterField(
            model_name="pharmacist2",
            name="PharmacistID",
            field=models.IntegerField(
                db_column="PharmacistID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="pharmacist2",
            name="PharmacistName",
            field=models.CharField(
                db_column="PharmacistName", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="pharmacist2",
            name="PharmacistSurname",
            field=models.CharField(
                db_column="PharmacistSurname", max_length=45, null=True
            ),
        ),
        migrations.AlterField(
            model_name="pharmacist2",
            name="Pharmacist_Phone",
            field=models.IntegerField(db_column="Pharmacist_Phone", null=True),
        ),
        migrations.AlterField(
            model_name="prescription2",
            name="MedicineName",
            field=models.CharField(db_column="MedicineName", max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="prescription2",
            name="Prescription_Code",
            field=models.CharField(
                db_column="Prescription_Code",
                max_length=45,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="prescription2",
            name="Prescription_Date",
            field=models.DateField(db_column="Prescription_Date", null=True),
        ),
        migrations.AlterField(
            model_name="prescription2",
            name="PresriptionCost",
            field=models.DecimalField(
                db_column="PresriptionCost", decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="specimen2",
            name="SpecimenID",
            field=models.IntegerField(
                db_column="SpecimenID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="specimen2",
            name="SpecimentType",
            field=models.CharField(
                db_column="SpecimentType", max_length=200, null=True
            ),
        ),
        migrations.AlterField(
            model_name="test2",
            name="Diagnosis",
            field=models.CharField(db_column="Diagnosis", max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="test2",
            name="NormalValue",
            field=models.DecimalField(
                db_column="NormalValue", decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="test2",
            name="SpecimenType",
            field=models.CharField(db_column="SpecimenType", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="test2",
            name="TestID",
            field=models.IntegerField(
                db_column="TestID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="test2",
            name="TestName",
            field=models.CharField(db_column="TestName", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="test2",
            name="TestUnitPrice",
            field=models.DecimalField(
                db_column="TestUnitPrice", decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="testresult2",
            name="TestResultID",
            field=models.IntegerField(
                db_column="TestResultID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="testresult2",
            name="Value",
            field=models.DecimalField(
                db_column="Value", decimal_places=2, max_digits=10
            ),
        ),
        migrations.AlterModelTable(
            name="appointment2",
            table="Appoinment2",
        ),
    ]
