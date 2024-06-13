from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

from .models import Patient, Doctor, Admin, Receptionist, LabAssistant, Pharmacist


def login_home(request):
    return render(request, 'homepage.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/hello')
    if request.method == 'POST':
        login_type = request.POST['login_type']
        username = request.POST['username']
        password = request.POST['password']

        if login_type == 'patient':
            try:
                user = Patient.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.PatientID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except Patient.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        elif login_type == 'doctor':
            try:
                user = Doctor.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.DoctorID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except Doctor.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        elif login_type == 'admin':
            try:
                user = Admin.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.AdminID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except Admin.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        elif login_type == 'receptionist':
            try:
                user = Receptionist.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.ReceptionistID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except Receptionist.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        elif login_type == 'pharmacist':
            try:
                user = Pharmacist.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.PharmacistID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except Pharmacist.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        elif login_type == 'lab_assistant':
            try:
                user = LabAssistant.objects.get(Username=username)
                if user.Password == password:
                    request.session['user_id'] = user.LabAssistantID
                    request.session['username'] = user.Username
                    return redirect('/hello')
                else:
                    error_message = 'Username or password is wrong. Please try again.'
            except LabAssistant.DoesNotExist:
                error_message = 'Username or password is wrong. Please try again.'

        return render(request, 'login_view.html', {'error': error_message})
    return render(request, 'login_view.html')
#####

def signup_view(request):
    if request.method == 'POST':
        user_type = request.POST['user_type']
        username = request.POST['username']
        name = request.POST['name']
        surname = request.POST['surname']
        countryCode = request.POST['countryCode']
        phoneNumber = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return render(request, "signup_view.html", {'error': 'Passwords do not match. Try again.'})

        phone = countryCode + phoneNumber

        if user_type == 'patient':
            if Patient.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(Patient.objects.latest('PatientID').PatientID)
                    patient_instance = Patient(Password=password, Username=username, PatientID=last_id + 1, Name=name,
                                               Surname=surname, Phone=phone)
                    patient_instance.save()
                except:
                    patient_instance = Patient(Password=password, Username=username, PatientID=1, Name=name,
                                               Surname=surname, Phone=phone)
                    patient_instance.save()

        elif user_type == 'doctor':
            if Doctor.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(Doctor.objects.latest('DoctorID').DoctorID)
                    doctor_instance = Doctor(Password=password, Username=username, DoctorID=last_id + 1, Name=name,
                                             Surname=surname, Phone=phone)
                    doctor_instance.save()
                except:
                    doctor_instance = Doctor(Password=password, Username=username, DoctorID=1, Name=name,
                                             Surname=surname, Phone=phone)
                    doctor_instance.save()

        elif user_type == 'admin':
            if Admin.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(Admin.objects.latest('AdminID').AdminID)
                    admin_instance = Admin(Password=password, Username=username, AdminID=last_id + 1, Name=name,
                                           Surname=surname, Phone=phone)
                    admin_instance.save()
                except:
                    admin_instance = Admin(Password=password, Username=username, AdminID=1, Name=name, Surname=surname,
                                           Phone=phone)
                    admin_instance.save()

        elif user_type == 'receptionist':
            if Receptionist.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(Receptionist.objects.latest('ReceptionistID').ReceptionistID)
                    receptionist_instance = Receptionist(Password=password, Username=username,
                                                         ReceptionistID=last_id + 1, Name=name, Surname=surname,
                                                         Phone=phone)
                    receptionist_instance.save()
                except:
                    receptionist_instance = Receptionist(Password=password, Username=username, ReceptionistID=1,
                                                         Name=name, Surname=surname, Phone=phone)
                    receptionist_instance.save()

        elif user_type == 'pharmacist':
            if Pharmacist.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(Pharmacist.objects.latest('PharmacistID').PharmacistID)
                    pharmacist_instance = Pharmacist(Password=password, Username=username, PharmacistID=last_id + 1,
                                                     Name=name, Surname=surname, Phone=phone)
                    pharmacist_instance.save()
                except:
                    pharmacist_instance = Pharmacist(Password=password, Username=username, PharmacistID=1, Name=name,
                                                     Surname=surname, Phone=phone)
                    pharmacist_instance.save()

        elif user_type == 'lab_assistant':
            if LabAssistant.objects.filter(Username=username).exists():
                return render(request, "signup_view.html", {'error': 'Username was taken before. Try again.'})
            else:
                try:
                    last_id = int(LabAssistant.objects.latest('LabAssistantID').LabAssistantID)
                    lab_assistant_instance = LabAssistant(Password=password, Username=username,
                                                          LabAssistantID=last_id + 1, Name=name, Surname=surname,
                                                          Phone=phone)
                    lab_assistant_instance.save()
                except:
                    lab_assistant_instance = LabAssistant(Password=password, Username=username, LabAssistantID=1,
                                                          Name=name, Surname=surname, Phone=phone)
                    lab_assistant_instance.save()

        return redirect('/login/')

    return render(request, 'signup_view.html')








from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment2, Patient2, Doctor2
from .forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment2.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment2, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

from django.shortcuts import render, redirect
from .models import Appointment2
from .forms import AppointmentForm

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.print_form()
            form.save()
            print("Form saved")
            return redirect('appointment_list')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment2, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment2, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})
