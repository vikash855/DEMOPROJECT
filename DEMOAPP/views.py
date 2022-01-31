from django.shortcuts import render
from DEMOAPP.models import RegisterData
from django.contrib import messages


def guest(request):
   request.session.clear()
   return render(request, 'users/guest.html')


# if i want to render html page without auth
def loginpage(request):
    if request.method == "POST":
        try:
            userdetails = RegisterData.objects.get(user=request.POST['user'], password=request.POST['password'])
            request.session['user'] = userdetails.user
            return render(request, 'users/guest.html')
        except RegisterData.DoesNotExist as e:
            messages.success(request, "User / Password Invalid")
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')


def registerdata(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        RegisterData(user=user, password=password).save()
        messages.success(request, 'the new user '+request.POST['user']+" Register Successfully")
        return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')


def forgotview(request):
    if request.method == "POST":
            users = request.POST['user']
            password1 = request.POST['password']
            password2 = request.POST['password1']
            userdetails = RegisterData.objects.get(user=request.POST['user'])
            if (password1 == password2 or users == userdetails):
                RegisterData.objects.filter(user=request.POST['user']).update(password=request.POST['password'])
                messages.success(request, "password Change Successfully")
                return render(request, 'users/forgot.html')
            else:
                messages.success(request, "Password is not same")
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


