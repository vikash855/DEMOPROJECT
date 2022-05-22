from django.shortcuts import render
from DEMOAPP.models import RegisterData
from django.contrib import messages


def guest(request):
    if request.method == "POST":
     request.session.clear()
     return render(request, 'users/guest.html')
    else:
     request.session.clear()
     return render(request, 'users/guest.html')

# if i want to render html page without auth
def loginpage(request):
    if request.method == "POST":
        try:
            logindetails = RegisterData.objects.get(user=request.POST['user'], password=request.POST['password'])
            request.session['user'] = logindetails.user
            return render(request, 'users/guest.html')
        except RegisterData.DoesNotExist:
            messages.success(request, "User / Password Invalid")
            return render(request, 'users/login.html')
    else:
        messages.success(request, "")
        return render(request, 'users/login.html')


def registerdata(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        try:
            RegisterData.objects.get(user=request.POST['user'])
            messages.success(request, "User Already Exist!")
            return render(request, 'users/register.html')
        except RegisterData.DoesNotExist:
            RegisterData(user=user, password=password).save()
            messages.success(request, 'the new user '+request.POST['user']+" Register Successfully" )
            return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')


def forgotview(request):
    if request.method == "POST":
        if (request.POST['password'] == request.POST['password1']):
            try:
                RegisterData.objects.get(user=request.POST['user'])
                RegisterData.objects.filter(user=request.POST['user']).update(password=request.POST['password'])
                messages.success(request, "Password Change Successfully")
                return render(request, 'users/forgot.html')
            except RegisterData.DoesNotExist:
                messages.success(request, "User Does't Exist!")
                return render(request, 'users/forgot.html')
        else:
            messages.success(request, "User/Password not matched")
            return render(request, 'users/forgot.html')
    else:
        return render(request, 'users/forgot.html')

def Approveview(request):
        if request.method == "POST":
            return render(request, 'users/Plant/Approve.html')
        else:
            return render(request, 'users/Plant/Approve.html')


def Entryview(request):
    if request.method == "POST":
        return render(request, 'users/Plant/Entry.html')
    else:
        return render(request, 'users/Plant/Entry.html')

def CHP11view(request):
    if request.method == "POST":
        return render(request, 'users/Plant/RRWeight.html')
    else:
        return render(request, 'users/Plant/RRWeight.html')
