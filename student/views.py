from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from student.models import Student 
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('show')
    if request.method == "POST":
        uid = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uid, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are Successfully Login"))
            return redirect('show' )
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again!! "))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def emp(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})

def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student': student})  
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show") 
    
def logout_views(request):
    logout(request)
    return redirect("")