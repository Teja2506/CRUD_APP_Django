from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import students
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def sms(request):
        student = students.objects.all()
        return render(request, 'sms.html', {'students':student})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
                login(request, user)
                return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
def logoutuser(request):
     logout(request)
     return redirect('/')

def addStudent(request):
     if request.method == 'POST':
          rollno = request.POST['rollno']
          name = request.POST['name']
          qualification = request.POST['qualification']
          course = request.POST['course']

          student = students()
          student.Roll_no = rollno
          student.Name = name
          student.Qualification = qualification
          student.Course_joined = course

          student.save()
          return redirect('sms')
     else:
          return render(request, 'sms.html')
     
def delStudent(request,id):
     student = students.objects.get(pk=id)
     student.delete()
     return redirect('sms')

def updateStudent(request, id):
    student = students.objects.get(pk=id)
    return render(request, 'updateStudent.html', {'std': student})

def updatedStudent(request, id):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        name = request.POST['name']
        qualification = request.POST['qualification']
        course = request.POST['course']

        std = students.objects.get(pk=id)
        std.Roll_no = rollno
        std.Name = name
        std.Qualification = qualification
        std.Course_joined = course

        std.save()
        return redirect('sms')
    
